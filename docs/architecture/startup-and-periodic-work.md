# Startup and periodic work

Tech & Res combines starting data with work performed when the game starts, time advances, or something happens. To change a feature safely, find both its initial state and the later code that updates it. A new value in a history file does not necessarily update an existing save.

## Starting a campaign

[common/history/global/ztr_global.txt](../../common/history/global/ztr_global.txt) contains a `GLOBAL` block that calls `create_tech_and_res_resource_deposits`, initializes each country's development, and triggers the initial economic update. It also starts selected French and Swiss events when those countries exist. Building history is separate under [common/history/buildings/](../../common/history/buildings/).

[ztr_starting_technologies.txt](../../common/history/global/ztr_starting_technologies.txt) repairs starting technology prerequisites, including Classicism/Romanticism and Physics/Atmospheric Engines. Its comment says it runs after the other relevant histories. [ztr_starting_technologies_historical.txt](../../common/history/global/ztr_starting_technologies_historical.txt) supplies further historical starting changes. Preserve those assumptions when changing prerequisites; this is not evidence that every existing-save case is handled.

The game-start hook in [ztr_map_modes_on_actions.txt](../../common/on_actions/ztr_map_modes_on_actions.txt) calls `ztr_map_modes_update`, which calls `ztr_mm_update_map_modes`. The same update is registered yearly. This supplies calculated information for journal map displays; it is separate from city-model selection.

## Work performed over time

[ztr_on_actions.txt](../../common/on_actions/ztr_on_actions.txt) registers named child actions rather than placing every system directly in one pulse. Its yearly list includes the main update, decolonization, UN institutions, nuclear work, and ideological-power updates. The main yearly effect manages capital-only special buildings and several political progression checks. Inspect the relevant child action and its called effects before changing frequency or conditions.

[ztr_demography_on_actions.txt](../../common/on_actions/ztr_demography_on_actions.txt) separates monthly initialization of untracked countries from yearly demographic updates. It also handles revolutions, secession, and released countries through dedicated effects. These actions have different scopes: for example, a released country is accessed through `scope:target`. Preserve the documented caller/callee scope rather than replacing it with a convenient global loop.

Journal entries also perform recurring work. [je_liberty_index](../../common/journal_entries/ztr_je_indexes.txt) updates liberty/equality values, political classifications, interest-group ideology, and progress bars on its yearly pulse. [The Research Center entries](../../common/journal_entries/ztr_je_technology.txt) combine availability checks, persistent variables, buttons, and project progress. Their updates are not all owned by the general on-action file.

## Event hooks and user actions

[ztr_harvest_condition_on_actions.txt](../../common/on_actions/ztr_harvest_condition_on_actions.txt) appends a child action to the game's harvest-condition hook. Its source explains why a second direct effect block would conflict with the existing game action. It also records a limitation: climate events infer the condition type from active regional conditions, so overlapping conditions can confuse that inference. Keep this documented uncertainty; it is not a verified runtime defect introduced by this task.

Buttons in [common/scripted_buttons/](../../common/scripted_buttons/) change state when selected. For example, Research Center projects check technology, country status, existing projects, and cooldowns before creating journal entries or variables. Feature settings in [ztr_game_rules.txt](../../common/game_rules/ztr_game_rules.txt) govern historical content, decolonization, population-related options, nuclear content, and climate disasters.

For an edit, trace **caller → condition → effect → stored variable/modifier → displayed result**. Check both new campaigns and existing saves where relevant. The [focused city tests](../../tests/info.md) do not test these wider systems. Follow the [editing guide](../development/editing-and-verification.md), and record what was inspected versus actually observed in game.
