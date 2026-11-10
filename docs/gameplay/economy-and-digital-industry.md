# Economy and digital industry

The mod adds industrial materials, consumer products and a connected data economy. Buildings buy inputs, produce goods and employ workers through their selected production methods. A good's definition alone does not explain how it is produced or used.

## Where the economy is defined

[New goods](../../common/goods/ztr_new_goods.txt) include ores, alloys, aluminium, plastics, refined fuels, electronics, processors, computers, robotics, water, pharmaceuticals, gas, civilian planes, space assets, data, software and AI systems. [Industrial buildings](../../common/buildings/ztr_industrial_buildings.txt) provide corresponding industries, including processor foundries, computer assembly, robotics, aircraft and space assets.

For each building, follow `production_method_groups` into [production-method groups](../../common/production_method_groups/), then follow their `production_methods` into [production methods](../../common/production_methods/). The group is the set of choices; each method specifies technology requirements, inputs, output and employment adjustments. Several selected groups contribute to one building's result.

Existing industries gain new choices through [modified vanilla buildings](../../common/buildings/ztr_vanilla_modified_buildings.txt) and [optimization additions](../../common/buildings/ztr_vanilla_optimization_buildings.txt). Preserve their `INJECT:` and `REPLACE:` directives. For example, `INJECT:building_glassworks` adds `pmg_data_optimization_light_industry` without supplying a complete new glassworks definition.

## Digital buildings and the data loop

[Digital buildings](../../common/buildings/ztr_digital_buildings.txt) define offices, software factories, interactive media, telecommunications, data centers and e-commerce logistics. Their unlocks include `market_studies`, `software_tech`, `videogames`, `telephone`, `digital_infrastructure` and `on_demand_delivery` respectively.

The main connections are implemented in [data production groups](../../common/production_method_groups/ztr_data_production_method_groups.txt) and [data production methods](../../common/production_methods/ztr_data_production_methods.txt):

1. Factories and other industries can report data. Early reporting produces `organized_data`. Later methods such as `pm_digital_data_on_premises_light_industry` produce `raw_data`, buy computers, software and business data, and add throughput.
2. Data centers use `pm_local_data_storage_building_datacenter` or cloud storage to turn raw data, water and electricity into organized data.
3. Offices use `pm_manual_market_studies` and later analysis/service methods to turn organized data into `business_data`. Other industries buy that business data to improve their operations.
4. Software factories supply `softwares`. Later development methods need more computers and telecommunications; `pm_vibe_coding_building_software_industry` also buys AI systems.
5. A data center can select model training to produce `ai_systems`. `pm_neural_model_training`, `pm_generative_ai_models` and `pm_artificial_general_intelligence` increase AI output while reducing organized-data output and adding electricity/water demand.

That last step uses negative `goods_output_organized_data_add` adjustments. It does not add a separate organized-data purchase. Keep this distinction when editing the training choices. Some methods similarly reduce their own building's output instead of buying that good back.

Government administration also produces data through methods such as `pm_advanced_data_networks` in [new production methods](../../common/production_methods/ztr_new_production_methods.txt). Universities have business-data output in their education methods. The digital economy therefore has several producers and feedback loops.

## Demand and related systems

Household demand depends on [population needs](../../common/pop_needs/ztr_pop_needs.txt), [additional needs](../../common/pop_needs/ztr_mr_pop_needs.txt) and [wealth purchase packages](../../common/buy_packages/ztr_buy_packages.txt), not just industrial inputs. Companies can specialize in these industries; see [companies and development](companies-and-development.md). Digital inputs also support [research](technology-and-research.md) and [electricity automation](energy-and-resources.md).

## Changing and checking this system

Trace a change from good to building, group, method, technology and consumer. Inspect all selected groups and employment scaling before claiming a building's final output. Keep local identifiers, input requirements, icons, modifiers and localization aligned. Follow [editing and verification](../development/editing-and-verification.md).

The connections above were checked in source, not through a running economy. No profitability, shortages, AI investment or late-game balance has been measured in this session. Commented-out production groups are not active choices merely because their definitions appear in a file.
