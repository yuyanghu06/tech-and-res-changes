# Military units, navies and nuclear systems

The mod extends the game's existing military units and formations into modern and future eras. Definitions connect technology, equipment goods, combat effects and illustrations. They do not establish that the AI can afford or correctly deploy every unlocked option.

## Land units and mobilization

[Infantry and marines](../../common/combat_unit_types/ztr_infantry_combat_unit_types.txt) extend vanilla upgrade lists with modern/advanced mechanized infantry and marines. Their technology requirements include mechanized_infantry, amphibious_warfare and high_performance_apparel. [Artillery](../../common/combat_unit_types/ztr_artillery_combat_unit_types.txt) adds self-propelled and rocket artillery. [Tank definitions](../../common/combat_unit_types/ztr_tank_combat_unit_types.txt) add modern light/heavy tanks, main battle tanks and a mecha unit.

Units consume goods such as refined fuel, electronics, processors, ammunition and tanks; the mecha unit also consumes robotics and AI systems. Battle and formation modifiers alter combat, movement, mobilization and invasion performance. Upgrade links, technology gates and goods supply must agree.

[Modern mobilization options](../../common/mobilization_options/ztr_new_mobilization_option.txt) add air support, paratroopers, modern medical support, missiles, helicopters, satellites/AWACS, nuclear artillery, electronic warfare, UAVs and AI drones. Definitions contain equipment-availability and exclusion conditions. Some equipment changes while mobilized reduce organization. Their [option groups](../../common/mobilization_option_groups/ztr_mobilization_option_groups.txt) determine presentation; [vanilla changes](../../common/mobilization_options/ztr_vanilla_mobilization_option.txt) alter existing options separately.

## Ships and customization

[Ship types](../../common/ship_types/ztr_navy_ship_types.txt) add modern cruisers, battleships, destroyers and troop ships, plus nuclear carriers/submarines. Each specifies construction goods, ongoing supplies, combat properties and compatible modifications. [Modern modifications](../../common/ship_modifications/ztr_navy_ship_modifications.txt) add propulsion, electronics and missile choices. Some slots reuse the game's existing modifications. Carrier air-wing slot examples are commented out; do not document them as available customization.

## Nuclear research and readiness

[Atomic journals](../../common/journal_entries/ztr_je_atomic.txt) track nuclear/thermonuclear programs and display arsenal information. Monthly research progress comes from [technology effects](../../common/scripted_effects/ztr_technology_scripts.txt), not the strike-damage file. Progress stops at 80% when other completion conditions remain unmet.

[Nuclear conditions](../../common/scripted_triggers/ztr_nuclear_triggers.txt) require appropriate technology, uranium law, sovereign status and operational facilities. An operational silo must be completed, staffed and free of goods shortages. Research pauses for default, an unavailable operational Research Center, nonproliferation commitments or the relevant treaty. Pauses preserve accumulated progress.

[Nuclear events](../../events/ztr_atomic.txt) grant or remove capability. Annual [maintenance hooks](../../common/on_actions/ztr_on_actions.txt) also handle old-save state and tested/captured silos. A launch-ready arsenal has a one-year cooldown. Range checks use strategic adjacency or the operational ICBM setup. [Strength values](../../common/script_values/ztr_nuclear_values.txt) combine facilities, staffing, technology, equipment and other country conditions.

## Diplomacy, strikes and limits

[War strikes](../../common/diplomatic_actions/ztr_war_nuclear_strike.txt), [unprovoked strikes](../../common/diplomatic_actions/ztr_unprovoked_nuclear_strike.txt), [ultimatums](../../common/diplomatic_actions/ztr_nuclear_ultimatum.txt) and [stationing agreements](../../common/diplomatic_actions/ztr_station_nuclear_weapons.txt) are different entry points. First-use political conditions and retaliation conditions differ. AI use is restricted; the unprovoked action is player-only.

[Strike effects](../../common/scripted_effects/ztr_atomic_scripts.txt) apply damage, retaliation and possible wider exchanges. Effects include population/building damage, devastation and timed modifiers. [Treaty articles](../../common/treaty_articles/) include de-escalation and research pauses. The legacy nuclear_warfare_system.99 event is labeled disabled and has no normal call found in this checkout; its definition is not proof of an active fallout feature.

Check [diplomacy](diplomacy-and-country-content.md), goods/production dependencies and [editing and verification](../development/editing-and-verification.md) together. None of these military flows was exercised in game during this work; current city-graphics tests do not verify combat, naval customization or nuclear exchanges.

## Performance implementation, 2026-11-10

Nuclear attack strength skips building scans for countries already excluded by missing nuclear capability, uranium policy or subject status. Eligible countries keep the original calculation order and final operational-silo check; defence strength is unchanged. Paused military research avoids unused progress arithmetic while still adding zero and applying the existing outer gates and clamps. See [the implementation record](../../milestones/behavior-preserving-performance/info.md). No update timing or stored campaign data changes.
