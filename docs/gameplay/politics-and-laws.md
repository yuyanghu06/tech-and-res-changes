# Politics and laws

The mod gives countries changing political views as they research modern ideas, become more developed and change their laws. It uses the game's existing interest groups, leaders, parties and movements. The feature definitions below are present in the source; their behavior has not been tested in a running game during this work.

## Scores, political direction and interest groups

Start with [je_liberty_index](../../common/journal_entries/ztr_je_indexes.txt). Its yearly update calls ztr_update_liberty_equality_index in [the main effects](../../common/scripted_effects/ztr_main_scripts.txt), then updates political direction, interest-group ideologies and social/environmental alignment.

[Political direction effects](../../common/scripted_effects/ztrpol_pole_effects.txt) begin after political_agitation. Liberty and Equality scores place a country in one of four groups: social, liberal, collectivist or reactionary. Initial dividing points are Liberty 50 and Equality 70. Subsequent changes require moving beyond a small buffer, so a country near a dividing point does not switch every year. These are country variables, not separate government laws.

[Interest-group conditions](../../common/scripted_triggers/ztrpol_ig_pole_triggers.txt) require a stable direction for four years and socialdemocracy before the relevant transformations. Clout conditions distinguish struggling groups. The larger [transformation effects](../../common/scripted_effects/ztrpol_ig_pole_effects.txt) and [transformation event](../../events/politics/ztrpol_ig_ideology_events.txt) choose and apply changes. Do not edit an event description and assume that changes the selection conditions.

The yearly global chain in [ztr_on_actions.txt](../../common/on_actions/ztr_on_actions.txt) separately adds and evolves social and environmental ideologies. Technology and national development both matter: human_rights and socialdemocracy introduce early opinions; counterculture, neoliberism, data_processing, ambientalism and circular_economy advance later sets.

## Leaders, parties and movements

[Modern leader ideologies](../../common/ideologies/ztrpol_leader_ideologies.txt) include democratic socialist, neoliberal, green, technocrat and national-populist choices. Each definition contains law preferences, country conditions and selection weights. [Leader eligibility conditions](../../common/scripted_triggers/ztrpol_leader_ideology_triggers.txt) specify which interest groups can supply them.

[Party definitions](../../common/parties/) replace vanilla party definitions and add green and populist parties. [Modern movements](../../common/political_movements/ztrpol_movements.txt) include environmental, antinuclear, civil-rights, digital-rights and democratization movements. Their [population-support factors](../../common/political_movement_pop_support/ztrpol_movement_pop_support.txt) connect pollution and international institutions to support. Law preferences, eligibility and popularity are separate pieces; check all three when changing political behavior.

## Laws and institutions

[Law groups](../../common/law_groups/ztr_laws.txt) add electricity systems, mining, uranium use, bioethics, data policy, LGBTQ rights, environmental protection and advanced education. Their [law definitions](../../common/laws/) supply conditions and effects. Many groups require both a technology and a national development level. Electricity-system changes are locked against ordinary enactment and are handled through their separate scripted content.

[Advanced education](../../common/laws/ztr_advanced_education.txt) adds secondary schooling and public universities. Child-labor and religious-school restrictions differ by law. [Environmental laws](../../common/laws/ztr_environmental_policy.txt) activate the environmental institution and connect to [climate](climate-and-environment.md). [UN standards](diplomacy-and-country-content.md) also constrain some existing laws.

Former Soviet law variants are no longer defined in [their old file](../../common/laws/ztr_russian_revolution_laws.txt); its comments direct readers to timed revolution modifiers.

## Editing and verification

Preserve scopes: a country, an interest group and its leader are different objects. Trace each condition to its caller and retain technology/development requirements. Several politics files name missing generators under scripts/politics; those generators are absent here. Do not claim regeneration is available. Follow [editing and verification](../development/editing-and-verification.md), update related localization, and distinguish source inspection from observed elections, ideology changes or enactment in game.

## Performance implementation, 2026-11-10

Environmental support now evaluates the state's pollution once during each population-support calculation. It saves and restores the support accumulated so far, reusing only temporary numbers for the existing threshold and multiplier. The policy inputs, description and update timing are unchanged. This is a narrow direct edit to generated output because the named generator is absent. See [the implementation record](../../milestones/behavior-preserving-performance/info.md) for checks and runtime limits.
