# Climate and environmental systems

The mod calculates global warming from countries' pollution and adds climate-sensitive disasters, journal information and events. Environmental policy affects both local conditions and the pollution counted by this model. A story about sea-level rise does not mean the script permanently changes the map's coastline.

## Temperature and pollution flow

[je_global_warming](../../common/journal_entries/ztr_je_global_warming.txt) initializes and updates the model yearly. [Climate effects](../../common/scripted_effects/ztr_global_warming_scripts.txt) sum countries' state pollution, apply reductions, record changes and update polluter rankings and disaster lists. ztr_global_warming_yearly_update owns this work.

The temperature calculation adds pollution-driven warming, subtracts a fraction of the accumulated anomaly and clamps the result between zero and six degrees above its baseline. [Stage conditions](../../common/scripted_triggers/ztr_main_triggers.txt) use thresholds above 0.5, 1.0, 1.5 and 2.0 degrees. [Stage events](../../events/ztr_global_warming_stages.txt) announce each crossed threshold once worldwide. A jump across several thresholds can announce each one.

The master ztr_global_warming_enabled condition currently returns yes. The separate [climate-disaster game rule](../../common/game_rules/ztr_game_rules.txt) controls disaster spawning and scaling; switching that rule off does not itself turn off the temperature journal/model.

## Disasters and event effects

[Climate harvest conditions](../../common/harvest_condition_types/ztr_climate_harvest_conditions.txt) add:

- Extreme heatwaves and megadroughts from stage 2.
- Hurricanes and extreme wildfires from stage 3.
- Prolonged coastal flooding from stage 4 in the specified low-lying-coast region.

Their definitions supply geographic/vulnerability conditions, duration, chance, intensity, incompatible conditions and economic or mortality effects. [Vanilla-condition changes](../../common/harvest_condition_types/ztr_vanilla_modified_harvest_conditions.txt) also make existing weather conditions climate-sensitive.

[Harvest-start hooks](../../common/on_actions/ztr_harvest_condition_on_actions.txt) append a separate action to the game's existing chain. They detect active conditions, save affected-country/state scopes and issue milestone or local events. The file notes that overlapping conditions can make detection imperfect because the event does not directly receive the new condition's type.

[Disaster events](../../events/ztr_global_warming.txt) let an affected country choose between greater devastation and paid relief for severe hurricanes or coastal flooding. Initial disasters can also be announced globally.

Permanent flooded-state traits, loss of arable land and direct coastal building removal are TODO comments in the coastal event. Current behavior includes long-lived harvest-condition penalties and devastation, not completed permanent land-loss mechanics.

## Environmental policy connections

[Environmental laws](../../common/laws/ztr_environmental_policy.txt) provide no protection, basic protection and active restoration. The stronger laws activate [institution_environmental_policy](../../common/institutions/ztr_environmental_policy.txt). The climate effects separately reduce counted pollution for environmental laws, institution investment, mining policy and urban_sustainability. Carbon capture is already included in states' pollution generation; do not subtract it a second time in the global total.

[Politics](politics-and-laws.md) supplies environmental ideologies and movements. [UN content](diplomacy-and-country-content.md) adds environmental standards and related requests. Their conditions can restrict law changes and affect support.

## Editing and verification

Read the warning at the top of [climate values](../../common/script_values/ztr_global_warming_values.txt): its temperature divisor, decay, ceiling and stage constants are reference values only. Runtime literals live in the climate effects and stage conditions. Editing the reference number alone changes no behavior. The harvest chance multiplier and intensity bonus in that values file are evaluated.

Keep global updates, stage checks, hazard definitions, hooks and localization aligned. Preserve rule guards and distinguish worldwide notices from affected-country effects. The current tests do not cover climate behavior. Follow [editing and verification](../development/editing-and-verification.md); observe pollution updates, a threshold crossing and an affected-state event in game before claiming the complete flow works.
