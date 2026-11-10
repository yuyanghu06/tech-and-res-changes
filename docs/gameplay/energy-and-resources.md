# Energy and resources

The mod adds deposits, extraction industries and several kinds of power generation. Its electricity system connects power plants to grid stations through a separate good named `global_electricity`, displayed as National Electricity. Technology, geography, laws and designated construction sites all affect what can be built.

## Resource creation and extraction

[Global startup history](../../common/history/global/ztr_global.txt) calls `create_tech_and_res_resource_deposits` in [resource creation effects](../../common/scripted_effects/ztr_resource_creation_scripts.txt). That effect calls explicit state-region lists for water/hydropower traits, copper and common-ore deposits, alongside other terrain-related effects. This is scripted placement, not automatic geological generation. See [startup and periodic work](../architecture/startup-and-periodic-work.md) before changing when it runs.

[Resource buildings](../../common/buildings/ztr_resources_buildings.txt) define water plants, bauxite, common-ore and advanced-ore mines, natural-gas rigs, rare-earth mines and hydroponics. [Additional resource buildings](../../common/buildings/ztr_mr_buildings.txt) supply the uranium-mine definition. Their production groups lead into extraction, transport, automation and by-product choices in [new production groups](../../common/production_method_groups/ztr_new_production_method_groups.txt) and [new production methods](../../common/production_methods/ztr_new_production_methods.txt).

State traits and building limits are defined in [extraction traits](../../common/state_traits/ztr_extraction_state_traits.txt), [additional traits](../../common/state_traits/ztr_mr_state_traits.txt) and [renewable traits](../../common/state_traits/ztr_renewable_state_traits.txt). Read the particular building's `potential`, `possible`, construction checks and maximum-level rules together; not every resource uses the same restriction.

## Electricity generation and distribution

[Energy buildings](../../common/buildings/ztr_energy_buildings.txt) define hydroelectric, renewable, geothermal and fusion plants plus `building_power_grid_station`. The ordinary power plant is replaced in [modified vanilla buildings](../../common/buildings/ztr_vanilla_modified_buildings.txt). Fission generation is a production method of that plant; the separate nuclear-plant building shown in comments is inactive.

[Energy production groups](../../common/production_method_groups/ztr_energy_production_method_groups.txt) and [methods](../../common/production_methods/ztr_energy_production_methods.txt) connect generation to two goods:

- Ordinary `electricity` supplies local building needs.
- `global_electricity`, defined in [new goods](../../common/goods/ztr_new_goods.txt), supplies grid stations. `pm_basic_grid_download`, `pm_hv_grid_download` and `pm_uhv_grid_download` consume it and produce ordinary electricity.

Generation choices change the proportions of these outputs as electricity-system laws advance. For example, the three `pm_run_of_river_plants` variants are tied to no national system, the national system and the modern national system. They are distinct law-selected methods, not interchangeable duplicate definitions.

## Establishing the grid

`start_national_electric_system_conversion_decision` in [energy decisions](../../common/decisions/ztr_energy_decisions.txt) requires `national_power_grid` and starts `je_national_electric_system` in [technology journal entries](../../common/journal_entries/ztr_je_technology.txt). [Energy effects](../../common/scripted_effects/ztr_energy_scripts.txt) count incorporated states with grid stations. Completion activates `law_national_electric_system` and a temporary transition modifier.

Grid-station construction can extend from the capital, generation sites or neighboring grid stations under its building conditions. The active journal entry also contains a yearly AI routine that creates missing stations. `modernize_national_electric_system_decision` later activates `law_modern_national_electric_system` after `high_voltage_transmission`; see [electricity laws](../../common/laws/ztr_national_electric_system.txt).

Hydropower requires the appropriate water trait and capacity. Geothermal construction requires the volcano check. Renewable plants require the national system. Fusion additionally needs `nuclear_fusion_reactor` and a designated site. Fission/fusion research or purchase routes connect to the [National Research Center](technology-and-research.md). Advanced automation consumes products from the [digital economy](economy-and-digital-industry.md).

## Changing and checking this system

Check deposits/traits, capacity, building conditions, technology, law, journal progress and every method variant together. Preserve output signs and law-specific visibility/replacement settings. A new-game placement change does not automatically update an existing save. Follow [editing and verification](../development/editing-and-verification.md).

These are inspected source connections. Grid conversion, resource availability, AI construction and generation balance have not been exercised in the running game during this work. Do not treat commented-out buildings or an icon as proof of an active feature.
