# Tech & Res repository instructions

This checkout is the full Victoria 3 Tech & Res mod. It lives directly in the game's user `mod` folder. Its `origin` is `https://github.com/yuyanghu06/tech-and-res-changes.git`; `main` tracks `origin/main`. Keep changes local unless the user requests publishing them.

## Start here and choose a system

These instructions apply to the entire mod. Read [the documentation index](docs/info.md), then the relevant system guide. [Feature status](docs/development/feature-status.md) distinguishes active source, inactive material, missing tools and actual verification. Active code takes precedence over comments or old changelogs.

| Area | Source starting points | Detailed guide |
| --- | --- | --- |
| Loading, identity and startup | `.metadata/`, `common/defines/`, `common/history/`, `common/on_actions/` | [Repository map](docs/architecture/repository-map.md); [startup and periodic work](docs/architecture/startup-and-periodic-work.md) |
| Technology and research programs | `common/technology/`, research journal/buttons/values/effects | [Technology and research](docs/gameplay/technology-and-research.md) |
| Goods, industries and digital services | `common/goods/`, `buildings/`, `production_method_groups/`, `production_methods/`, `pop_needs/`, `buy_packages/` | [Economy and digital industry](docs/gameplay/economy-and-digital-industry.md) |
| Electricity and resources | Energy/resource buildings, energy decisions/effects and electricity laws | [Energy and resources](docs/gameplay/energy-and-resources.md) |
| Companies and development | `common/company_types/`, `prestige_goods/`, development values/effects/journal | [Companies and development](docs/gameplay/companies-and-development.md) |
| Politics, laws and interest groups | Laws, law groups, ideologies, parties, movements and `ztrpol_*` scripts | [Politics and laws](docs/gameplay/politics-and-laws.md) |
| Population and demographic transition | `ztr_demography_*`, population journals/events and growth defines | [Demographics](docs/gameplay/demographics.md) |
| UN, diplomacy and country paths | Treaty articles, diplomatic actions/plays, journals and events | [Diplomacy and country content](docs/gameplay/diplomacy-and-country-content.md) |
| Army, navy and nuclear programs | Combat units, ship types/equipment, atomic/nuclear scripts | [Military and nuclear systems](docs/gameplay/military-and-nuclear.md) |
| Climate and environmental effects | Global-warming journal, effects, values, triggers and events | [Climate and environment](docs/gameplay/climate-and-environment.md) |
| City, fleet and battlefield appearance | `gfx/map/`, `gfx/models/`, city graphics triggers | [Cities and military models](docs/visuals/cities-and-military-models.md) |
| Panels, text, icons and thumbnails | Journals, scripted buttons/GUIs/progress bars, localization, inline icons and metadata | [Interface, localization and metadata](docs/visuals/interface-localization-and-metadata.md) |

The guides give exact repository-relative paths. Filenames often begin with `ztr_`, but many identifiers are inherited or unprefixed. Preserve exact names and search their references throughout the mod.

## Trace the whole change

- For technologies, trace prerequisites, research restrictions, building/method unlocks, history grants, related journal entries, AI, text and icons. Era date comments are not calendar restrictions; the current end date is defined separately in `common/defines/ztr_defines.txt`.
- For economic features, follow building → production-method group → method → goods, jobs and modifiers. Also inspect consumers, population needs, company conditions and AI. One selected method does not describe a whole building's final output.
- For political, population or diplomatic features, find the active caller and scope. Follow conditions, values, effects, country/state variables, timed modifiers and cleanup. Preserve initialization for new countries and the frequency of periodic work.
- For military changes, check units, upgrades, equipment, goods, technology gates and AI separately from pictures and map models. For climate, inspect the runtime calculation; similarly named reference values may not control it.
- For interface and visual work, keep localization keys, icons, mesh/entity names and file paths connected. Most controls are journal entries; `gui/` currently holds inline icon definitions. Preserve geography/technology/DLC selection and building requirements. Detailed city rules are in the visual guide; the existing unrelated African test entries were outside the Russian fix.

Preserve native patch prefixes such as `INJECT:`, `TRY_INJECT:`, `REPLACE:` and `REPLACE_OR_CREATE:`. Inspect the target/base definition and established local examples before changing them. Do not invent a blanket filename-priority rule or casually turn patches into duplicate ordinary definitions.

## Editing and checking

Keep work within the requested behavior. Preserve existing identifiers, encodings, byte-order marks and line endings. Localization files may require a UTF-8 byte-order mark. Avoid reformatting large files or replacing binary assets incidentally.

Some city files reference `scripts/city_gen/` generators and a design document that are absent from this checkout. Historical technology comments also cite absent audit documents. Do not invent regeneration/build commands. A folder named `unused` or `backup` is not proof the engine ignores it; inspect references before deleting anything.

Use [the editing and verification guide](docs/development/editing-and-verification.md). Run `git diff --check`. The existing focused suite is `python -B -m unittest discover -s tests -v`; [tests/info.md](tests/info.md) explains its fixed baseline. The six city tests cover Russian city source selection; eight performance tests compare focused original/current script calculations and UN orchestration. These tests do not establish the entire mod's runtime behavior, rendering, saved-game compatibility or city refresh after research. For other systems, check the full caller/condition/calculation/effect path and related identifiers; use actual in-game observations before claiming gameplay or visual correctness. Clearly separate source inspection, automated checks and observed behavior.

Preserve mod ID `tech.res` in `.metadata/metadata.json`; its supported game version is `1.15.*` and dependency list is empty. Filenames such as `ztr_mr_*` alone do not prove an external dependency. `.metadata/thumbnail.png` is the user-confirmed launcher image; the mod's separate DLC-style presentation lives under `dlc/dlc_ztr/`. Paid-pack checks such as `ip5_cosmetics` are distinct.

Use installed game files read-only at `C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game` for native examples. Do not incidentally modify installed game/Workshop files, launcher databases, playsets, saves, sibling mods or personal configuration. Never read or copy sibling `.env` files as routine work. Upstream ignores still exclude `scripts/`, `CLAUDE.md` and `LOG.md`; requested `docs/` and AGENTS.md are eligible for versioning.

## Shared workflow and records

Follow the user's shared plan, implement, test, evaluate, fix and integrate workflow. Use the shared roles under `~/.codex/agents/` and `~/.codex/AGENT_WORKFLOW.md` when installed; neither was available when this checkout was initialized. Do not duplicate shared role definitions or change agent registrations here. Specialists must have exclusive file ownership and must not spawn more agents. If independent checking is unavailable, say so.

Keep dated user notes in `notes.md`. After each meaningful pass, update `milestones/milestone.md` and `milestones/to-do.md`, append an immutable America/New_York timestamped entry under `milestones/history/` using `docs/templates/history-entry.md`, and refresh affected folder `info.md` guides. Only the primary agent writes shared journals during delegated work. Record actual checks, remaining limitations and the next action. Preserve existing records and other active milestones. Update the relevant system guide when behavior changes.
