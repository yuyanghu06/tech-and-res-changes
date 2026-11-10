# Technology and research

Tech & Res extends the technology tree and gives countries a National Research Center for scientific cooperation and major research projects. Ordinary technology unlocks, the center's operating methods, and its special projects are separate systems; trace all three before changing research behavior.

## Technology definitions and dates

[Technology files](../../common/technology/technologies/) contain military, production and society definitions. Files named `ztr_new_*` hold ordinary additions; `ztr_modified_vanilla_*`, `ztr_mr_*` and `ztr_modified_mr_*` also patch or supply definitions using prefixes such as `INJECT:`, `REPLACE:` and `REPLACE_OR_CREATE:`. Preserve the prefix as well as the identifier.

[00_eras.txt](../../common/technology/eras/00_eras.txt) defines eleven eras and their research costs. Its date comments run from before 1836 through 2032–2051. Those comments describe intended periods, not calendar gates. The actual configured `END_DATE` is `2036.1.1` in [ztr_defines.txt](../../common/defines/ztr_defines.txt). Do not advertise a supported campaign through 2051 from the era comments.

The inspected source contains 235 ordinary definitions across the three `ztr_new_*` files and 57 other definition/patch blocks. These are source counts, not the final number of technologies after the game and DLC definitions load.

## Research Center flow

1. `research_center_decision` in [unique building decisions](../../common/decisions/ztr_unique_buildings_decision.txt) starts a site survey after `verrier_modern_physics_tech` and the required administrative, academic and site checks.
2. `je_research_center_site` and the construction entry in [technology journal entries](../../common/journal_entries/ztr_je_technology.txt) lead to a permitted site for `building_research_center` in [unique buildings](../../common/buildings/ztr_unique_buildings.txt).
3. Operating the center makes `je_research_center` available. Its [buttons](../../common/scripted_buttons/ztr_research_center_buttons.txt) launch nuclear weapons, thermonuclear, nuclear power and fusion projects, or change research philosophy. Conditions prevent overlapping projects and apply cooldowns.

[Research values](../../common/script_values/ztr_research_values.txt) calculate `country_research_progress` from twice the academic-base level, development tier plus two, and capped research-agreement points. Academic levels use absolute literate population in [literacy checks](../../common/scripted_triggers/ztr_literacy_trigger.txt). See [companies and development](companies-and-development.md) for the economic tier.

The active philosophy scales modifiers in [technology modifiers](../../common/static_modifiers/ztr_technology_modifiers.txt): independent research increases maximum innovation while reducing technology spread; absorption increases spread. [Technology effects](../../common/scripted_effects/ztr_technology_scripts.txt) set philosophy, its ten-year change cooldown and project progress. The building's own inputs and innovation output live separately in [unique-building production methods](../../common/production_methods/ztr_unique_buildings_production_methods.txt).

## Cooperation and special routes

The active `ztr_research_agreement` [treaty article](../../common/treaty_articles/ztr_research_agreement.txt) requires Research Centers, suitable relations and peace between the parties. Partner rank and relations affect capacity gains; [agreement values](../../common/script_values/ztr_research_agreement_values.txt) also guide AI acceptance. The separate [quick diplomatic proposal](../../common/diplomatic_actions/ztr_propose_research_agreement.txt) is commented out and disabled.

`nuclear_reactor` has `can_research = no` in [production technologies](../../common/technology/technologies/ztr_new_production.txt). Its routes are the center's nuclear-power program or a purchase through [energy decisions](../../common/decisions/ztr_energy_decisions.txt), not ordinary research selection. Conversely, `pm_computerized_research_center` is a university method despite its name; [vanilla production groups](../../common/production_method_groups/ztr_vanilla_production_method_groups.txt) attach it to universities.

## Changing and checking this system

Check prerequisites, building and production-method unlocks, project conditions, localization and [starting grants](../../common/history/global/ztr_starting_technologies.txt) together. Technology names also control [city appearance](../../common/scripted_triggers/ztr_city_graphics_triggers.txt). Follow [startup and periodic work](../architecture/startup-and-periodic-work.md) and [editing and verification](../development/editing-and-verification.md).

This guide records inspected source. Research projects, treaty acceptance, economic effects and campaign progression have not been verified in the running game during this work. Existing city tests do not establish research-system correctness.

## Performance implementation, 2026-11-10

The Research Center's over-cap agreement display uses raw points minus the cap with a zero floor, avoiding a second treaty traversal. Contributions and agreement limits are unchanged. Paused nuclear and thermonuclear programs add zero before evaluating an unused gain; the existing goal gates and later 80% clamps retain their original positions. See [the implementation record](../../milestones/behavior-preserving-performance/info.md); no saved variables, update dates or gameplay settings are introduced.
