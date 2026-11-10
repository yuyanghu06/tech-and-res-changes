# Gameplay definitions and shared scripts

This folder contains most game rules and content. Start with [the documentation index](../docs/info.md) and [the repository map](../docs/architecture/repository-map.md).

- `technology`, `goods`, `buildings`, `building_groups`, `production_method_groups`, `production_methods`, `pop_needs` and `buy_packages` connect unlocks, industries, jobs, goods and consumers.
- `company_types`, `prestige_goods` and development scripts connect companies, branded output and national economic development.
- Laws, law groups, institutions, ideologies, parties, movements, diplomatic definitions and treaty articles define political and international choices.
- Combat units, ship types, ship modifications/slots and mobilization definitions describe military gameplay. Their appearance is selected under `gfx` separately.
- `history` initializes the world. `on_actions` registers recurring work and callbacks for changes such as country creation; journal entries and events have additional callers.
- `scripted_triggers` checks conditions, `script_values` calculates numbers and `scripted_effects` changes state. Buttons, scripted GUIs, progress bars and customizable localization support journal controls.

Trace a feature through its caller, scope, shared helpers, related definitions and displayed text. Preserve native patch prefixes and saved-state ownership. [Editing and verification](../docs/development/editing-and-verification.md) explains the required checks and current test limits.
