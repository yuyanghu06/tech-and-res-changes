# Editing and verification

Use this guide to make the requested change and gather evidence for the behavior it affects. The engine reads game content directly; there is no application build step that proves the scripts or models work.

## Trace before editing

Start in [the relevant guide](../info.md). Search an exact identifier across the engine-facing folders, for example:

```powershell
rg -n --fixed-strings 'building_research_center' common events gfx gui localization
```

Find its definition, conditions, consumers, updates and cleanup. Check the scope: a country, a state, a state region, a building and a company are different owners of data. Shared `scripted_triggers` answer conditions, `script_values` calculate numbers, and `scripted_effects` change game state. Trace the caller before changing a shared helper; it may serve journal entries, recurring callbacks and country events at once.

Preserve the established `INJECT:`, `TRY_INJECT:`, `REPLACE:` or `REPLACE_OR_CREATE:` pattern. Inspect the installed base-game definition read-only when needed. The [repository map](../architecture/repository-map.md) gives examples; a filename alone is not a universal priority rule.

## Check the affected path

| Area | Follow the change through |
| --- | --- |
| Technologies/research | Prerequisites, normal versus scripted research, unlocks, starting grants, program conditions/progress, AI, text/icons |
| Buildings/goods/energy | Building groups, allowed locations, production groups/methods, employment, inputs/outputs, law variants, demand and company links |
| Politics/demography | Law/ideology eligibility, indexes, saved variables, periodic updates, stage modifiers and newly created country initialization |
| Diplomacy/country content | Initiating action or journal, scopes, participant conditions, votes/cooldowns, resolution, releases/war cleanup and localization |
| Military/nuclear | Unit/ship upgrades and costs, equipment, technology, operational-building checks, range/retaliation and AI; artwork is separate |
| Climate | Actual temperature/stage calculations, policy modifiers, disaster game rule, geographic conditions, harvest effects and one-time flags |
| Visuals/text | Definitions and references, city/entity selection, all required assets, localization BOM/header/keys and displayed result |

Do not expand a focused fix into unrelated edge handling, balance changes or formatting. Preserve other writers' changes. Keep generated-file edits narrow: the upstream city generators and cited design/audit documents are absent, so no regeneration command is available here.

## Available automated checks

```powershell
git diff --check
python -B -m unittest discover -s tests -v
```

[The test guide](../../tests/info.md) explains the six city tests and eight focused performance tests. They read the actual city scripts and check technology stages, pack/geography fallbacks, skyscraper requirements and preserved content. Their preservation baseline is fixed at the imported commit, rather than the moving `HEAD`. The performance tests compare the actual baseline/current arithmetic and effect flow across 929 paired fixtures, with explicit deterministic boundaries for UN scoring and separate preservation checks. Both evaluators interpret only the constructs needed for their checks; they are not the game engine or a general mod validator.

For other changes, inspect script structure, duplicate definitions, exact cross-references and the full behavior path. Validate referenced meshes/entities against `.asset` declarations. Do not report a clean diff, a parser result or an asset match as proof of gameplay, balance, appearance or automatic refresh after research. For documentation, check local links and cited source paths against the actual files.

## Runtime evidence and records

Observe the specific behavior when a suitable game session is available. Do not alter a user's running campaign, playsets, databases, saves, other mods or personal settings incidentally. Record the game/mod context and exactly what was observed; if no such check ran, say so. [Feature status](feature-status.md) records the current boundary.

Update the relevant guide, `notes.md`, milestone snapshot/work list, and affected `info.md` pages. Append an immutable history record using [the template](../templates/history-entry.md). Shared journals belong to the primary agent during delegated work; preserve other active investigations. Keep commits and publication within the user's requested scope.
