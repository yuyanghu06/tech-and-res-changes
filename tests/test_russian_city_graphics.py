"""Focused source checks; this is not a replacement for the game renderer."""

from collections import Counter
from dataclasses import dataclass, replace
from pathlib import Path
import re
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
IMPORTED_BASELINE_COMMIT = "38b0685472188a42ca7dee4adb047b6a0b4c61f6"
CITY_DIR = Path("gfx/map/city_data/city_types")
CP_DIR = Path("gfx/map/city_data/city_centerpiece")
BASE_PATH = CITY_DIR / "ztr_eeu_city.txt"
RUSSIAN_PATH = CITY_DIR / "ztr_eeu_russian_city.txt"
RUSSIAN_CP_PATH = CP_DIR / "ztr_eeu_russian_cities.txt"
TOKEN = re.compile(r'\s+|\#[^\n]*|"(?:\\.|[^"\\])*"|\?=|>=|<=|!=|[{}=<>]|[^\s{}=<>?#]+')
OPERATORS = {"=", "?=", ">", "<", ">=", "<=", "!="}


class Block(list):
    """Ordered statements and list items, retaining duplicate keys."""


def parse(text):
    tokens = []
    position = 0
    for match in TOKEN.finditer(text.lstrip("\ufeff")):
        if match.start() != position:
            raise ValueError("Unrecognized script text")
        position = match.end()
        token = match.group()
        if token.isspace() or token.startswith("#"):
            continue
        tokens.append(token[1:-1] if token.startswith('"') else token)
    index = 0

    def read(nested=False):
        nonlocal index
        result = Block()
        while index < len(tokens):
            token = tokens[index]
            index += 1
            if token == "}":
                if not nested:
                    raise ValueError("Unexpected closing brace")
                return result
            if index < len(tokens) and tokens[index] in OPERATORS:
                operator = tokens[index]
                index += 1
                value = tokens[index]
                index += 1
                if value == "{":
                    value = read(True)
                result.append((token, operator, value))
            else:
                result.append(token)
        if nested:
            raise ValueError("Missing closing brace")
        return result

    return read()


def read_source(path):
    return parse((ROOT / path).read_text(encoding="utf-8-sig"))


def statements(block):
    return [entry for entry in block if isinstance(entry, tuple)]


def values(block, key):
    return [value for name, _, value in statements(block) if name == key]


def one(block, key, default=None):
    result = values(block, key)
    if len(result) > 1:
        raise ValueError(f"Duplicate singleton {key}")
    return result[0] if result else default


def definitions(block):
    result = {}
    for name, operator, value in statements(block):
        if name in result or operator != "=" or not isinstance(value, Block):
            raise ValueError(f"Invalid/duplicate definition {name}")
        result[name] = value
    return result


def walk(block):
    for entry in statements(block):
        yield entry
        if isinstance(entry[2], Block):
            yield from walk(entry[2])


@dataclass(frozen=True)
class Situation:
    technologies: frozenset = frozenset()
    dlc: bool = True
    russian_area: bool = True
    socialist: bool = False
    state: str = "STATE_MOSCOW"
    regions: frozenset = frozenset({"geographic_region_russia"})
    building: bool = False
    building_type: str = "building_skyscraper"
    level: int = 0
    construction: bool = False


def evaluate(block, situation, triggers):
    """Evaluate only the conditions exercised here, rejecting unknown syntax."""
    results = []
    for key, operator, value in statements(block):
        if key == "OR":
            result = any(evaluate(Block([entry]), situation, triggers) for entry in statements(value))
        elif key in {"NOT", "NOR"}:
            result = not any(evaluate(Block([entry]), situation, triggers) for entry in statements(value))
        elif key in {"AND", "any_scope_state", "owner"}:
            result = evaluate(value, situation, triggers)
        elif key == "any_scope_building":
            result = situation.building and evaluate(value, situation, triggers)
        elif key == "b(building_skyscraper)":
            result = evaluate(value, situation, triggers) if situation.building else operator == "?="
        elif key == "state_has_building_type_levels":
            result = (one(value, "target") == "bt:building_skyscraper" and situation.building
                      and evaluate(Block([entry for entry in statements(value) if entry[0] == "value"]),
                                   situation, triggers))
        elif key in {"level", "value"}:
            left, right = situation.level, int(value)
            result = {">": left > right, "=": left == right, ">=": left >= right}[operator]
        elif key == "is_under_construction":
            result = situation.construction == (value == "yes")
        elif key == "is_building_type":
            result = situation.building and value == situation.building_type
        elif key == "has_technology_researched":
            result = value in situation.technologies
        elif key == "has_dlc_feature":
            result = situation.dlc and value == "ip5_cosmetics"
        elif key == "russian_buildings_trigger":
            result = situation.russian_area == (value == "yes")
        elif key == "balkan_buildings_trigger":
            result = False
        elif key == "ztr_is_communist":
            result = situation.socialist == (value == "yes")
        elif key == "is_in_geographic_region":
            result = value in situation.regions
        elif key == "this":
            result = value == "s:" + situation.state
        elif key in triggers:
            result = evaluate(triggers[key], situation, triggers) == (value == "yes")
        else:
            raise ValueError(f"Unsupported test condition {key} {operator} {value}")
        results.append(result)
    return all(results)


class RussianCityGraphicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = definitions(read_source(BASE_PATH))
        cls.russian = definitions(read_source(RUSSIAN_PATH))
        cls.centerpieces = definitions(read_source(RUSSIAN_CP_PATH))
        cls.triggers = definitions(read_source("common/scripted_triggers/ztr_city_graphics_triggers.txt"))
        cls.candidates = {}
        for path in (BASE_PATH, RUSSIAN_PATH, CITY_DIR / "ztr_city_test.txt"):
            cls.candidates.update(definitions(read_source(path)))

    def select_city(self, situation):
        eligible = [(int(one(body, "weight", "0")), name)
                    for name, body in self.candidates.items()
                    if evaluate(one(body, "trigger", Block()), situation, self.triggers)]
        if not eligible:
            return None
        highest = max(weight for weight, _ in eligible)
        winners = [name for weight, name in eligible if weight == highest]
        self.assertEqual(len(winners), 1, winners)
        return winners[0]

    def test_only_eastern_europe_test_overrides_were_removed(self):
        for path in (CITY_DIR / "ztr_city_test.txt", CP_DIR / "ztr_city_test.txt"):
            with self.subTest(path=path):
                original = subprocess.check_output(
                    ["git", "show", IMPORTED_BASELINE_COMMIT + ":" + path.as_posix()], cwd=ROOT)
                before = definitions(parse(original.decode("utf-8-sig")))
                after = definitions(read_source(path))
                removed = {name for name in before if name.startswith("ztr_city_test_eeu_")}
                self.assertEqual(len(removed), 8)
                self.assertEqual(after, {name: body for name, body in before.items() if name not in removed})
        for folder in (CITY_DIR, CP_DIR):
            for path in (ROOT / folder).glob("*.txt"):
                self.assertNotRegex(path.read_text(encoding="utf-8-sig"), r"(?m)^ztr_city_test_eeu_\w*\s*=")

    def test_other_production_city_and_hub_definitions_unchanged(self):
        for path in (BASE_PATH, CITY_DIR / "ztr_eeu_hubs.txt", CP_DIR / "ztr_eeu_cities.txt",
                     CP_DIR / "ztr_eeu_hubs.txt"):
            original = subprocess.check_output(
                ["git", "show", IMPORTED_BASELINE_COMMIT + ":" + path.as_posix()], cwd=ROOT)
            self.assertEqual(definitions(parse(original.decode("utf-8-sig"))), definitions(read_source(path)), path)

    def test_variants_keep_original_gates_and_custom_building_proportions(self):
        expected_bases = {name for name in self.base if name.startswith("ztr_eeu_city_")}
        actual_bases = {name.replace("ztr_eeu_russian_city_", "ztr_eeu_city_", 1) for name in self.russian}
        self.assertEqual(actual_bases, expected_bases)
        for name, body in self.russian.items():
            with self.subTest(city=name):
                base = self.base[name.replace("ztr_eeu_russian_city_", "ztr_eeu_city_", 1)]
                gate = one(body, "trigger")
                self.assertEqual(one(gate, "has_dlc_feature"), "ip5_cosmetics")
                self.assertEqual(one(gate, "russian_buildings_trigger"), "yes")
                inherited_gate = Block([entry for entry in gate if entry[0] not in
                                        {"has_dlc_feature", "russian_buildings_trigger"}])
                self.assertEqual(inherited_gate, one(base, "trigger"))
                self.assertGreater(int(one(body, "weight")), int(one(base, "weight")))
                for pool in ("rich_building_meshes", "mid_building_meshes", "poor_building_meshes"):
                    original, current = one(base, pool), one(body, pool)
                    self.assertEqual(Counter(v for v in original if v.startswith("ztr_")),
                                     Counter(v for v in current if v.startswith("ztr_")))
                    self.assertEqual(len(original), len(current))
                    historical = [v for v in current if not v.startswith("ztr_")]
                    self.assertTrue(historical)
                    self.assertTrue(all(v.startswith("russian_") for v in historical), historical)
                for key, _, val in statements(body):
                    if key.startswith("building_"):
                        self.assertFalse(any(isinstance(v, str) and v.startswith("european_") for v in val))

    def test_selection_before_and_through_all_six_technology_stages(self):
        stages = [("elevator", "early_modern_start"), ("paved_roads", "early_modern"),
                  ("highway_systems", "late_modern"), ("multinational_corporations", "postmodern"),
                  ("circular_economy", "digital"), ("agentic_ai", "ai")]
        for socialist in (False, True):
            for dlc in (False, True):
                for native_area in (False, True):
                    context = Situation(socialist=socialist, dlc=dlc, russian_area=native_area)
                    self.assertIsNone(self.select_city(context), "Modern mod city selected without technology")
                    learned = set()
                    for tech, stage in stages:
                        learned.add(tech)
                        context = replace(context, technologies=frozenset(learned))
                        suffix = stage + ("_socialist" if socialist and stage not in {"early_modern_start", "ai"} else "")
                        prefix = "ztr_eeu_russian_city_" if dlc and native_area else "ztr_eeu_city_"
                        with self.subTest(socialist=socialist, dlc=dlc, native_area=native_area, tech=tech):
                            self.assertEqual(self.select_city(context), prefix + suffix)
        outside = Situation(technologies=frozenset(tech for tech, _ in stages),
                            regions=frozenset({"geographic_region_canada"}), state="STATE_ONTARIO")
        self.assertIsNone(self.select_city(outside))

    def test_centerpiece_links_and_no_skyscraper_without_a_building(self):
        links = Counter()
        for name, body in self.centerpieces.items():
            for city in values(body, "city_graphics_type"):
                self.assertIn(city, self.russian)
                links[city] += 1
            entities = [value for key, _, value in walk(body) if key == "entity"]
            if any("skyscraper" in entity for entity in entities):
                gate = one(body, "trigger")
                self.assertIsNotNone(gate, name)
                for building, level, construction, expected in ((False, 0, False, False),
                                                               (True, 0, False, False),
                                                               (True, 1, False, True),
                                                               (True, 0, True, True)):
                    with self.subTest(centerpiece=name, building=building, level=level, construction=construction):
                        context = Situation(building=building, level=level, construction=construction)
                        self.assertEqual(evaluate(gate, context, self.triggers), expected)
                self.assertFalse(evaluate(gate, Situation(building=True, building_type="building_university", level=3),
                                          self.triggers), "Another building must not satisfy the skyscraper requirement")
                for key, _, value in walk(body):
                    if key == "variant" and any("skyscraper" in str(entity) for entity in values(value, "entity")):
                        self.assertEqual(one(value, "building_type"), "building_skyscraper")
        self.assertEqual(set(links), set(self.russian))
        self.assertTrue(all(count == 2 for count in links.values()))

    def test_historical_centerpiece_retains_native_separate_attachments(self):
        historical = [body for body in self.centerpieces.values()
                      if "ztr_eeu_russian_city_early_modern_start" in values(body, "city_graphics_type")]
        self.assertEqual(len(historical), 2)
        for body in historical:
            attachments = values(body, "attach")
            self.assertEqual(len(attachments), 2)
            self.assertTrue(all(len(values(attach, "variant")) == 1 for attach in attachments))


if __name__ == "__main__":
    unittest.main(verbosity=2)
