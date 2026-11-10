"""Compare focused current scripts with the fixed imported source.

This deliberately small evaluator uses Decimal arithmetic, explicit fixture scopes
and the actual parsed scripts. It is not the game engine or a timing benchmark.
UN orchestration tests substitute deterministic country preparation/law scoring;
separate AST checks establish that the real preparation/scoring code is retained.
Unsupported operations raise rather than silently succeeding.
"""

from collections import Counter
from copy import deepcopy
from dataclasses import dataclass, field
from decimal import Decimal
from itertools import product
import subprocess
import unittest

from test_russian_city_graphics import (
    Block, IMPORTED_BASELINE_COMMIT, ROOT, definitions, one, parse, statements,
)


D = Decimal
POLITICS = "common/political_movements/ztrpol_movements.txt"
POLLUTION = "common/script_values/ztrpol_movement_values.txt"
RESEARCH = "common/script_values/ztr_research_values.txt"
PROGRESS = "common/scripted_effects/ztr_technology_scripts.txt"
NUCLEAR = "common/script_values/ztr_nuclear_values.txt"
UN = "common/scripted_effects/ztr_un_law_opinion_functions.txt"


def source(path, baseline=False):
    if baseline:
        text = subprocess.check_output(
            ["git", "show", f"{IMPORTED_BASELINE_COMMIT}:{path}"],
            cwd=ROOT,
        ).decode("utf-8-sig")
    else:
        text = (ROOT / path).read_text(encoding="utf-8-sig")
    return definitions(parse(text))


@dataclass
class Scope:
    values: dict = field(default_factory=dict)
    variables: dict = field(default_factory=dict)
    flags: dict = field(default_factory=dict)
    collections: dict = field(default_factory=dict)


class Script:
    """Only the arithmetic, conditions and effects exercised below."""

    COLLECTIONS = {
        "every_scope_state": "states", "every_scope_building": "buildings",
        "any_scope_building": "buildings", "any_rival_country": "rivals",
        "any_scope_treaty": "treaties", "any_scope_article": "articles",
    }
    MEMBERSHIP = {
        "has_technology_researched": "technologies", "has_modifier": "modifiers",
        "has_law": "laws", "has_law_or_variant": "laws",
        "has_active_production_method": "methods",
    }

    def __init__(self, root, formulas=None, effects=None, numbers=None, globals_=None):
        self.root = root
        self.formulas = formulas or {}
        self.effects = effects or {}
        self.numbers = numbers or {}
        self.globals = globals_ or {}
        self.temporary = {}
        self.counts = Counter()
        self.descriptions = []
        self.effect_overrides = {}
        self.law_core = None
        self.score_boundary = None

    def scope(self, name, current):
        if name == "root":
            return self.root
        if name.startswith("scope:"):
            return self.temporary[name[6:]]
        return current.values[name]

    def number(self, value, current):
        if isinstance(value, Block):
            return self.math(value, current)
        try:
            return D(value)
        except Exception:
            pass
        if "." in value:
            head, tail = value.split(".", 1)
            return self.number(tail, self.scope(head, current))
        if value.startswith("var:"):
            return current.variables[value[4:]]
        if value.startswith("global_var:"):
            return self.globals[value[11:]]
        if value.startswith("scope:"):
            return self.temporary[value[6:]]
        if value in self.numbers:
            self.counts[value] += 1
            return D(self.numbers[value])
        if value in self.formulas:
            self.counts[value] += 1
            return self.math(self.formulas[value], current)
        if value in current.values:
            return D(current.values[value])
        raise ValueError(f"Unsupported numeric input: {value}")

    def condition(self, block, current):
        return all(self.test(key, op, value, current) for key, op, value in statements(block))

    def test(self, key, op, value, current):
        if key in {"OR", "NOR"}:
            result = any(self.test(k, o, v, current) for k, o, v in statements(value))
            return result if key == "OR" else not result
        if key in {"AND", "NOT"}:
            result = self.condition(value, current)
            return result if key == "AND" else not result
        if key in {"owner", "state", "root"} or key.startswith("scope:") and isinstance(value, Block):
            return self.condition(value, self.scope(key, current))
        if key in self.COLLECTIONS:
            collection = current.collections[self.COLLECTIONS[key]]
            return any(self.condition(value, child) for child in collection)
        if key in self.MEMBERSHIP:
            return value in current.values[self.MEMBERSHIP[key]]
        if key == "has_variable":
            return value in current.variables
        if key == "has_global_variable":
            return value in self.globals
        if key == "exists":
            if value.startswith("scope:"):
                return value[6:] in self.temporary
            raise ValueError(f"Unsupported exists: {value}")
        if key == "institution_investment_level":
            institution = one(value, "institution")
            condition = next(item for item in statements(value) if item[0] == "value")
            return self.compare(D(current.values["institutions"][institution]), condition[1], D(condition[2]))
        if key == "country_ship_type_fraction":
            target = one(value, "target")
            condition = next(item for item in statements(value) if item[0] == "value")
            return self.compare(D(current.values["ship_fractions"][target]), condition[1], D(condition[2]))
        if key in current.flags:
            return current.flags[key] == (value == "yes")
        if key in {"is_pop_type", "strata", "military_wage_level", "has_type"}:
            return current.values[key] == value
        return self.compare(self.number(key, current), op, self.number(value, current))

    @staticmethod
    def compare(left, op, right):
        if op in {"=", "?="}:
            return left == right
        if op == "!=":
            return left != right
        if op == ">":
            return left > right
        if op == "<":
            return left < right
        if op == ">=":
            return left >= right
        if op == "<=":
            return left <= right
        raise ValueError(f"Unsupported comparison: {op}")

    def selected(self, block, current):
        """Yield operations with native if / else_if / else chaining."""
        matched = None
        for key, op, value in statements(block):
            if key in {"if", "else_if", "else"}:
                if key == "if":
                    matched = False
                elif matched is None:
                    raise ValueError("Unattached else branch")
                if not matched and (key == "else" or self.condition(one(value, "limit"), current)):
                    matched = True
                    if value is self.law_core:
                        self.score_boundary(current)
                    else:
                        yield from self.selected(value, current)
            else:
                matched = None
                if key != "limit":
                    yield key, op, value

    def math(self, block, current=None, initial=D(0)):
        current = current or self.root
        result = initial
        for key, op, value in self.selected(block, current):
            if key == "desc":
                self.descriptions.append(value)
            elif key == "save_temporary_value_as":
                self.temporary[value] = result
            elif key in {"every_scope_state", "every_scope_building"}:
                for child in current.collections[self.COLLECTIONS[key]]:
                    self.counts[key] += 1
                    if self.condition(one(value, "limit", Block()), child):
                        result = self.math(value, child, result)
            elif key in {"value", "add", "subtract", "multiply", "divide", "min", "max"}:
                operand = self.number(value, current)
                if key == "value":
                    result = operand
                elif key == "add":
                    result += operand
                elif key == "subtract":
                    result -= operand
                elif key == "multiply":
                    result *= operand
                elif key == "divide":
                    result /= operand
                elif key == "min":
                    result = max(result, operand)
                elif key == "max":
                    result = min(result, operand)
            else:
                raise ValueError(f"Unsupported arithmetic: {key}")
        return result

    def effect(self, block, current=None):
        current = current or self.root
        for key, op, value in self.selected(block, current):
            if key in {"set_variable", "set_global_variable"}:
                target = self.globals if key == "set_global_variable" else current.variables
                if isinstance(value, Block):
                    target[one(value, "name")] = self.number(one(value, "value"), current)
                else:
                    target[value] = D(1)
            elif key in {"remove_variable", "remove_global_variable"}:
                target = self.globals if key == "remove_global_variable" else current.variables
                target.pop(value, None)
            elif key == "change_variable":
                name = one(value, "name")
                operations = Block(item for item in statements(value) if item[0] != "name")
                current.variables[name] = self.math(operations, current, current.variables[name])
            elif key == "clamp_variable":
                name = one(value, "name")
                current.variables[name] = min(
                    self.number(one(value, "max"), current),
                    max(self.number(one(value, "min"), current), current.variables[name]),
                )
            elif value == "yes" and key in self.effect_overrides:
                self.counts[key] += 1
                self.effect_overrides[key](current)
            elif value == "yes" and key in self.effects:
                self.counts[key] += 1
                self.effect(self.effects[key], current)
            else:
                raise ValueError(f"Unsupported effect: {key}")


class PerformanceOptimizations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = {path: source(path, True) for path in (POLITICS, POLLUTION, RESEARCH, PROGRESS, NUCLEAR, UN)}
        cls.new = {path: source(path) for path in cls.old}

    def pair(self, path, root, *, formulas=None, numbers=None):
        extra = formulas or {}
        return [Script(deepcopy(root), {**version[path], **extra}, numbers=numbers)
                for version in (self.old, self.new)]

    def test_environmental_support_and_explanations(self):
        # Entire actual weight, including profession, literacy, radicals and poles.
        for pollution, profession, policy, pole in product(
            ("0", "1999.999", "2000", "2000.001", "6000", "10000", "20000"),
            ("academics", "farmers", "laborers"), (False, True), ("social", "none"),
        ):
            country = Scope(values={
                "laws": {"law_type:law_active_restoration"} if policy else set(),
                "institutions": {"institution_environmental_policy": 5 if policy else 0},
                "technologies": {"urban_sustainability"} if policy else set(),
            }, flags={
                "ztrpol_un_environment_norm": policy,
                "ztrpol_is_social_pole": pole == "social",
                "ztrpol_is_collectivist_pole": False,
                "ztrpol_is_reactionary_pole": False,
            })
            state = Scope(values={"owner": country, "pollution_generation": D(pollution),
                                  "state_population": D(1000000), "state_urbanization_rate": D("0.6")})
            pop = Scope(values={"state": state, "owner": country, "is_pop_type": profession,
                                "strata": "lower", "literacy_rate": D("0.7"),
                                "pop_radical_fraction": D("0.4")})
            runs = [Script(deepcopy(pop), version[POLLUTION]) for version in (self.old, self.new)]
            weights = [one(version[POLITICS]["movement_ztrpol_environmentalist"], "pop_support_weight")
                       for version in (self.old, self.new)]
            with self.subTest(pollution=pollution, profession=profession, policy=policy, pole=pole):
                self.assertEqual(runs[0].math(weights[0]), runs[1].math(weights[1]))
                self.assertEqual(runs[0].descriptions, runs[1].descriptions)
                self.assertEqual(runs[1].counts["ztrpol_state_pollution_per_million"], 1)
                self.assertEqual(runs[0].counts["ztrpol_state_pollution_per_million"],
                                 1 + int("ztrpol_movement_pollution" in runs[0].descriptions))
                self.assertEqual(runs[0].root.variables, runs[1].root.variables)

    def test_research_agreement_cap_and_formula_evaluation_count(self):
        for raw, funded in product(("0", "0.001", "5.999", "6", "6.001", "7.999", "8", "8.001", "20.125"), (False, True)):
            root = Scope(values={"technologies": {"funded_research_projects"} if funded else set()})
            runs = [Script(deepcopy(root), version[RESEARCH], numbers={"ztr_research_agreements_raw": raw})
                    for version in (self.old, self.new)]
            with self.subTest(raw=raw, funded=funded):
                results = [run.number("ztr_research_agreements_over_cap", run.root) for run in runs]
                self.assertEqual(*results)
                self.assertGreaterEqual(results[1], 0)
                self.assertEqual(runs[0].counts["ztr_research_agreements_raw"], 2)
                self.assertEqual(runs[1].counts["ztr_research_agreements_raw"], 1)

    def test_paused_and_running_nuclear_progress_preserves_caps(self):
        for effect, variable, goals, cap, technology in (
            ("nuclear_development_add_progress", "nuclear_development_var", "ztr_nuclear_weapons_goals_met", 1200, "atomic_bomb"),
            ("thermonuclear_development_add_progress", "thermonuclear_development_var", "ztr_thermonuclear_weapons_goals_met", 1600, "second_nuclear_reactor"),
        ):
            for paused, met, progress, capacity, rush, researched in product(
                (False, True), (False, True), (0, cap - 1, cap, cap + 1),
                ("2", "19.25"), ("none", "rival", "war"), (False, True),
            ):
                rival = Scope(values={"modifiers": {"nuclear_capability"}}, variables={"thermonuclear_capability_var": D(1)})
                root = Scope(values={"technologies": {technology} if researched else set()},
                             variables={variable: D(progress)},
                             flags={goals: met, "ztr_nuclear_research_paused": paused, "is_at_war": rush == "war"},
                             collections={"rivals": [rival] if rush == "rival" else []})
                runs = [Script(deepcopy(root), effects=version[PROGRESS], numbers={"country_research_progress": capacity})
                        for version in (self.old, self.new)]
                with self.subTest(program=effect, paused=paused, met=met, progress=progress,
                                  capacity=capacity, rush=rush, researched=researched):
                    for run, version in zip(runs, (self.old, self.new)):
                        run.effect(version[PROGRESS][effect])
                    self.assertEqual(runs[0].root.variables, runs[1].root.variables)
                    expected_calls = int(not paused and (met or progress < cap))
                    self.assertEqual(runs[1].counts["country_research_progress"], expected_calls)

    def test_nuclear_strength_exclusions_and_eligible_calculation(self):
        technologies = {"guided_missiles", "anti_satellite_weapons", "directed_energy_weapons",
                        "electronic_warfare", "network_centric_warfare", "cyber_warfare", "stealth_technology", "ai_warfare"}
        for capable, law, subject, operational, ai, wage, reduced in product(
            (False, True), (False, True), (False, True), (False, True),
            (False, True), ("very_low", "normal", "very_high"), (False, True),
        ):
            country = Scope(values={"technologies": technologies, "gdp": D(4000000000),
                "get_country_gdp_per": D(30), "military_wage_level": wage,
                "laws": {"law_type:law_uranium_full_usage"} if law else set(),
                "modifiers": ({"nuclear_capability"} if capable else set()) | {"ztr_superpower"} | ({"recently_reduced_nukes"} if reduced else set()),
                "ship_fractions": {"ship_type:ship_type_nuclear_submarine": D("0.5")}},
                flags={"is_subject": subject, "is_ai": ai, "ztr_has_operational_nuclear_silo": operational},
                collections={"treaties": []})
            silo = Scope(values={"owner": country, "occupancy": D("0.75"),
                                "methods": {"pm_hydrogen_bomb", "pm_nuclear_stockpile_3", "pm_icbms"}},
                         flags={"ztr_is_operational_nuclear_silo": operational})
            country.collections["states"] = [Scope(collections={"buildings": [silo]})]
            runs = self.pair(NUCLEAR, country)
            with self.subTest(capable=capable, law=law, subject=subject, operational=operational,
                              ai=ai, wage=wage, reduced=reduced):
                results = [run.number("ztr_nuclear_attack_strength", run.root) for run in runs]
                self.assertEqual(*results)
                self.assertEqual(runs[1].counts["every_scope_building"], int(capable and law and not subject))
                if capable and law and not subject and operational:
                    self.assertGreater(results[1], 0)
                else:
                    self.assertEqual(results[1], 0)

    def un_parts(self):
        original = self.old[UN]["ztr_un_value_law"]
        cleanup = self.new[UN]["ztr_un_value_law_clear_country_context"]
        cleanup_entries = statements(cleanup)
        # The helper excludes only init/preparation and the original final cleanup.
        expected = Block(item for item in statements(original)
                         if item[0] not in {"ztr_un_init_governance_laws", "ztr_un_value_law_prepare_country_context"})
        for entry in cleanup_entries:
            self.assertEqual(entry[0], "remove_variable")
            self.assertIn(entry, expected)
            # Remove the last matching occurrence; initial per-score resets remain.
            index = max(i for i, item in enumerate(expected) if item == entry)
            expected.pop(index)
        return original, cleanup_entries, expected

    def test_un_real_scoring_and_preparation_preserved(self):
        original, cleanup, expected = self.un_parts()
        self.assertEqual(self.new[UN]["ztr_un_value_law_from_prepared_context"], expected)
        self.assertEqual(self.old[UN]["ztr_un_value_law_prepare_country_context"],
                         self.new[UN]["ztr_un_value_law_prepare_country_context"])
        self.assertEqual(len(cleanup), 21)
        for name in ("ztr_un_set_current_law_as_considered", "ztr_un_set_possible_law_as_considered",
                     "ztr_un_set_current_vote_law_as_considered", "ztr_un_set_vote_proposal_as_considered"):
            self.assertEqual(self.old[UN][name], self.new[UN][name])

    def un_run(self, version, *, subject=1, scores=(0, 30), months=6, eligible=True,
               settled=False, can_propose=True, profile=2):
        cleanup = statements(self.new[UN]["ztr_un_value_law_clear_country_context"])
        names = [entry[2] for entry in cleanup]
        root = Scope(variables={"unrelated": D(37), "ztr_un_vote_choice_neutral": D(1)},
                     flags={"ztr_un_country_can_propose_possible_law": can_propose,
                            "ztr_un_is_not_applied_law": True})
        if eligible:
            root.variables["ztr_un_vote_eligible"] = D(1)
        if settled:
            root.variables["ztr_un_vote_choice_support"] = D(1)
        globals_ = {"ztr_un_subject_possible_proposal": D(subject), "ztr_un_law_possible_proposal": D(2),
                    "ztr_un_vote_subject": D(subject), "ztr_un_vote_proposal": D(2),
                    "ztr_un_vote_months_remaining": D(months)}
        # Derive all current-law global keys from the real selector, avoiding a
        # duplicate hand-maintained subject/law table in the test.
        selector = self.old[UN]["ztr_un_set_current_law_as_considered"]
        for _, _, branch in statements(selector):
            if isinstance(branch, Block):
                for key, _, assignment in statements(branch):
                    if key == "set_variable":
                        ref = one(assignment, "value")
                        if ref.startswith("global_var:"):
                            globals_[ref[11:]] = D(1)
        run = Script(root, effects=version[UN], globals_=globals_)
        run.trace = []
        original = self.old[UN]["ztr_un_value_law"]
        # There is one large considered-law conditional. Identify it by its
        # required variables rather than its thousands of law-specific branches.
        old_core = next(value for key, _, value in statements(original) if key == "if"
                        and [v for k, _, v in statements(one(value, "limit")) if k == "has_variable"]
                        == ["ztr_un_subject_considered", "ztr_un_law_considered"])
        scorer = version[UN].get("ztr_un_value_law_from_prepared_context", version[UN]["ztr_un_value_law"])
        run.law_core = next(value for key, _, value in statements(scorer) if key == "if" and value == old_core)

        def prepare(current):
            for index, name in enumerate(names):
                current.variables[name] = D(profile + index)
            current.variables["liberty_index_var"] = D(profile * 10)

        def score(current):
            if not all(name in current.variables for name in names):
                raise AssertionError("Scoring ran without its prepared country data")
            law = current.variables["ztr_un_law_considered"]
            amount = D(scores[0 if law == 1 else 1])
            # Exercise actual objective/secret summation and clamps afterward.
            current.variables["ztr_un_law_value_objective_considered"] = amount - D(profile)
            current.variables["ztr_un_law_value_secret_considered"] = D(profile)
            current.variables["ztr_un_value_law_considered_un_role"] = D(3)
            run.trace.append(("score", current.variables["ztr_un_subject_considered"], law, amount))

        def start(current):
            run.globals["ztr_un_vote_in_progress"] = D(1)

        run.score_boundary = score
        run.effect_overrides = {
            "ztr_un_init_governance_laws": lambda current: None,
            "ztr_un_prioritize_first_institution_establishment_vote": lambda current: None,
            "ztr_un_value_law_prepare_country_context": prepare,
            "ztr_un_start_governance_vote": start,
        }
        return run

    def test_un_proposal_comparison_decision_cleanup_and_work(self):
        for subject, scores, can_propose in product(range(1, 14), ((0, 30), (30, 0), (0, 0), (-150, 150)), (False, True)):
            runs = [self.un_run(version, subject=subject, scores=scores, can_propose=can_propose)
                    for version in (self.old, self.new)]
            with self.subTest(subject=subject, scores=scores, eligible=can_propose):
                for run in runs:
                    run.effect(run.effects["ztr_un_ai_try_start_possible_vote"])
                self.assertEqual(runs[0].root.variables, runs[1].root.variables)
                self.assertEqual(runs[0].globals, runs[1].globals)
                self.assertEqual(runs[0].trace, runs[1].trace)
                self.assertEqual(runs[0].counts["ztr_un_value_law_prepare_country_context"], 2 if can_propose else 0)
                self.assertEqual(runs[1].counts["ztr_un_value_law_prepare_country_context"], int(can_propose))

    def test_un_neutral_voter_decision_thresholds_cleanup_and_work(self):
        for subject, months, scores, eligible, settled in product(
            (1, 8, 13), (1, 6), ((0, 13), (0, 14), (0, 25), (25, 0), (0, 0), (-150, 150)),
            (False, True), (False, True),
        ):
            runs = [self.un_run(version, subject=subject, scores=scores, months=months,
                                eligible=eligible, settled=settled) for version in (self.old, self.new)]
            with self.subTest(subject=subject, months=months, scores=scores, eligible=eligible, settled=settled):
                for run in runs:
                    run.effect(run.effects["ztr_un_ai_take_neutral_vote_position"])
                self.assertEqual(runs[0].root.variables, runs[1].root.variables)
                self.assertEqual(runs[0].globals, runs[1].globals)
                self.assertEqual(runs[0].trace, runs[1].trace)
                active = eligible and not settled
                self.assertEqual(runs[0].counts["ztr_un_value_law_prepare_country_context"], 2 if active else 0)
                self.assertEqual(runs[1].counts["ztr_un_value_law_prepare_country_context"], int(active))

    def test_un_public_single_law_entry_remains_self_contained(self):
        for score in (-150, 0, 150):
            runs = [self.un_run(version, scores=(score, 20)) for version in (self.old, self.new)]
            for run in runs:
                run.root.variables.update(ztr_un_subject_considered=D(1), ztr_un_law_considered=D(1))
                run.effect(run.effects["ztr_un_value_law"])
            self.assertEqual(runs[0].root.variables, runs[1].root.variables)
            self.assertEqual(runs[0].trace, runs[1].trace)
            self.assertEqual(runs[1].counts["ztr_un_value_law_prepare_country_context"], 1)


if __name__ == "__main__":
    unittest.main()
