# Repository map

This checkout is the full Tech & Res mod. Victoria 3 reads its game-data folders directly; there is no separate server or application build. Keep the mod rooted in its own folder under the game's user `mod` directory. The installed game's files and Steam Workshop copies are references, not editing destinations.

## Find the part that owns the behavior

| Location | What it contains |
| --- | --- |
| [common/](../../common/) | Technologies, buildings, goods, production, politics, countries, recurring calculations, and other gameplay definitions. |
| [events/](../../events/) | Events and their choices, including country stories and international systems. |
| [localization/](../../localization/) | Names, descriptions, tooltips, and other displayed text. |
| [gui/](../../gui/) | Two inline text-icon definition files; most mod control panels are journal entries instead. |
| [gfx/](../../gfx/) | Building and military models, map definitions, pictures, icons, videos, and asset declarations. |
| [.metadata/](../../.metadata/) | Launcher identity, compatibility information, and the local-mod thumbnail. |
| [dlc/](../../dlc/) and [dlc_metadata/](../../dlc_metadata/) | The mod's separate DLC-style presentation and registration. |
| [tests/](../../tests/info.md) | Focused checks for the Russian city change, not a whole-mod test suite. |

Inside `common/`, follow a feature across its data rather than assuming one file contains everything. A building in [buildings/](../../common/buildings/) references production-method groups, whose methods consume or produce goods and may require technologies. Journal entries can call scripted buttons, triggers, effects, progress bars, and localization. Country and global history establish starting conditions; on-actions and event chains perform later updates. See [startup and periodic work](startup-and-periodic-work.md).

## Definitions and patch prefixes

New definitions often use `ztr_` identifiers, but many technologies, buildings, and text keys use inherited or unprefixed names. Preserve the actual identifier and all its references.

Existing files demonstrate four explicit patch forms:

- `REPLACE:ai_strategy_resource_expansion` in [ztr_admin_strategies.txt](../../common/ai_strategies/ztr_admin_strategies.txt) supplies a replacement definition.
- `INJECT:ai_strategy_default` in [ztr_default_strategy.txt](../../common/ai_strategies/ztr_default_strategy.txt) adds changes to an existing target.
- `REPLACE_OR_CREATE:building_uranium_mine` in [ztr_mr_buildings.txt](../../common/buildings/ztr_mr_buildings.txt) uses a replacement-or-creation form.
- `TRY_INJECT:wealth_10` in [ztr_buy_packages.txt](../../common/buy_packages/ztr_buy_packages.txt) uses an optional injection form.

These are source examples, not a complete engine specification. Inspect the current target and nearby patterns before choosing a form. Do not infer a universal load order from a `ztr_` filename. The [compatibility triggers](../../common/scripted_triggers/ztr_compatibility_triggers.txt) expose hooks such as `technres_is_active` for other mods; the launcher dependency list is currently empty.

## Boundaries and current limits

[Metadata](../../.metadata/metadata.json) targets game `1.15.*`. [Defines](../../common/defines/ztr_defines.txt) set the end date to **2036-01-01**, while comments in [the technology-era definitions](../../common/technology/eras/00_eras.txt) describe a final era through **2051**. Those comments do not establish a later configured end date.

Several city files reference generators under `scripts/city_gen/` and a design document absent from this checkout. Do not invent a regeneration command. Filenames containing `mr`, `unused`, or `backup` are not proof of dependencies or inactive content. Read references and conditions. Use the [editing and verification guide](../development/editing-and-verification.md) before changing data or assets; distinguish source-defined features from behavior observed in the game.
