# Companies and development

Companies connect named businesses to industries, technologies, locations and bonuses. National development separately tracks economic output per person and changes construction conditions, company capacity and research strength. These systems meet through the country's economy, but they use different definitions and update rules.

## Company definitions

[Company types](../../common/company_types/) contain sector-specific businesses and changes to existing regional companies. Sectors include technology, vehicles, pharmaceuticals, mining, oil/gas, consulting, cosmetics, furniture, media, e-commerce and textiles. Many files patch existing companies with `INJECT:` or `REPLACE:`; others define ordinary new identifiers. Preserve those distinctions.

For each company, inspect `building_types`, extension industries, location and technology conditions, prosperity bonuses, AI construction targets and possible prestige goods. These fields need not name exactly the same industries.

For example, `company_asml` in [technology companies](../../common/company_types/ztr_tech_companies.txt) has robotics as its main industry and processor foundries as an extension. Its establishment conditions include `mechatronics` and an incorporated Holland state with a sufficiently developed electronics industry. Its prosperity bonuses affect processor and electronics throughput. Do not simplify all these relationships into “ASML is an electronics building.”

## Prestige goods

[Prestige goods](../../common/prestige_goods/ztr_prestige_goods.txt) and [generic prestige goods](../../common/prestige_goods/ztr_generic_prestige_goods.txt) define branded or specialized versions of base goods. Company definitions list which they may produce. For example, `prestige_good_asml_euv_lithography_machines` uses `robotics` as its base good and requires `mp1_content`.

Some goods have additional progress through [prestige-good journal entries](../../common/journal_entries/ztr_je_prestige_goods.txt). The `je_ztr_prestige_good_generic_records_and_films` example selects a suitable prosperous company, checks national production rank, advances a monthly timer and sets a company variable on completion. [Messages](../../common/messages/ztr_prestige_goods_messages.txt) and [journal localization](../../localization/english/ztr_prestige_goods_je_l_english.yml) explain the outcome. Inspect each entry's own conditions; not every company or good follows that example.

## National development flow

[General values](../../common/script_values/ztr_general_value.txt) define `get_country_gdp_per` as GDP divided by population. [Development values](../../common/script_values/ztr_development_values.txt) classify countries into levels 0–8 and set separate thresholds for rising and falling, so small movements around one boundary do not necessarily reverse a recent change.

[Development effects](../../common/scripted_effects/ztr_development_scripts.txt) store the level in `ztr_development_level_var`. Initialization assigns the appropriate tier; subsequent annual checks move it by at most one tier. [Global history](../../common/history/global/ztr_global.txt) initializes starting countries. [On-actions](../../common/on_actions/ztr_on_actions.txt) perform yearly updates and monthly initialization for countries that lack a level. [Development announcement events](../../events/ztr_main_events.txt) report changes; they are not the owner of the tier calculation.

`je_development` in [development journal entries](../../common/journal_entries/ztr_je_development.txt) applies the current tier's modifier and presents its map/status. [Economy modifiers](../../common/static_modifiers/ztr_economy_modifiers.txt) change construction costs/speed, bureaucracy investment cost and maximum company count; later tiers also reduce mortality. Use active values rather than conflicting old comments when explaining numbers.

Development tier plus two contributes to `country_research_progress` in [research values](../../common/script_values/ztr_research_values.txt). Academic strength and agreements supply the other parts; see [technology and research](technology-and-research.md). Inputs and consumers of company industries are covered in [economy and digital industry](economy-and-digital-industry.md).

## Changing and checking these systems

Trace company requirements, industry lists, bonuses, prestige-good base goods, DLC conditions, journal variables, icons and localization together. For development, keep initial classification, promotion/demotion thresholds, annual scheduling, modifiers and displayed status aligned. Follow [startup and periodic work](../architecture/startup-and-periodic-work.md) and [editing and verification](../development/editing-and-verification.md).

This guide describes inspected definitions. Company establishment, prosperity, prestige-good awards and development transitions have not been tested in the running game during this work. Metadata's empty dependency list does not remove individual definitions' DLC requirements.
