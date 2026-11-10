# Diplomacy and country content

The mod adds international agreements, UN decisions and historical or alternate country paths. Entry points matter: a definition may be active through a decision, journal or periodic event, while another file contains only future country data.

## UN membership, votes and institutions

[UN decisions](../../common/decisions/ztr_un_decisions.txt) cover the Geneva Convention, League of Nations, UN founding, membership and withdrawal. The founding decision requires the top-ranked country, international_organizations and a date after 1944. [Foundation events](../../events/international_organizations/un_events.txt) initialize governance and membership.

[je_un_info_panel and je_un_votations](../../common/journal_entries/ztr_je_un.txt) provide menus and an active voting session. [UN effects](../../common/scripted_effects/ztr_un_scripts.txt) use shared global variables for the proposal, eligible countries, choices, weights and results. Sessions last six months, then resolve and start a four-year cooldown. Support must exceed opposition; ties fail. When veto rights are enabled, permanent-member opposition can block adoption.

Voting models are one country/one vote, rank-weighted voting, permanent members only, or the two highest-prestige UN members. Proposal topics include governance, decolonization, slavery, children's and women's rights, environmental/labor standards, and IMF, WTO, ICC and UNESCO establishment. [Compliance events](../../events/international_organizations/ztr_un_compliance_events.txt) and [compliance effects](../../common/scripted_effects/ztr_un_compliance_scripts.txt) handle follow-up requests and standards. Some minimum laws are imposed; other reforms are requested. Read the particular effect before claiming membership instantly changes every law.

[IMF modernization](../../common/journal_entries/ztr_je_un_institutions.txt) adds aid-related actions and events with literacy, living-standard and economic completion goals.

## Agreements and peaceful consolidation

[Research agreements](../../common/treaty_articles/ztr_research_agreement.txt) are active treaty articles requiring Research Centers, acceptable relations and peace between partners. The [old diplomatic shortcut](../../common/diplomatic_actions/ztr_propose_research_agreement.txt) is commented out.

[Peaceful country unification](../../common/diplomatic_actions/ztr_unify_countries.txt) annexes an accepting small neighbor under cultural, territorial, prestige and political conditions from [the shared conditions](../../common/scripted_triggers/ztr_main_triggers.txt). Its actual technology requirement is international_organizations; the file's neoimperialism header is stale. [Power-bloc merging](../../common/diplomatic_actions/ztr_merge_power_bloc_diplomacy.txt) is active and requires neoimperialism. These are distinct from future continental superstates.

## Country paths and decolonization

- [Russia](../../common/journal_entries/ztr_je_russia_soviet.txt): post-1910 autocratic-monarchy hardship leads to competing order, liberal and Soviet progress, petitions and possible peripheral collapse. [Russian effects](../../common/scripted_effects/ztr_russian_scripts.txt) and [events](../../events/russia/russian_revolution.txt) apply the outcomes.
- [China](../../common/journal_entries/ztr_je_china.txt): corporate, federal and techno-Confucian paths follow the surviving-Qing route. [The vanilla journal replacement](../../common/journal_entries/ztr_vanilla_je.txt) connects the post-1940 outcome. Communist/Nationalist fronts and final-war resolution also use [monthly hooks](../../common/on_actions/ztr_on_actions.txt).
- [Austria](../../common/journal_entries/ztr_je_austria.txt), [the Ottomans](../../common/journal_entries/ztr_je_turkey.txt) and [Ireland](../../common/journal_entries/ztr_je_ireland.txt) have pressure/collapse or independence journals. Austria's old disabling line is commented, so it does not disable the definition.
- [Arabian unification](../../common/journal_entries/ztr_je_arabia.txt) tracks Nejd's control of Nejd, Hedjaz and Hail. [US](../../events/usa/usa_economy.txt), [Japanese](../../events/japan/japan_economy.txt) and [Swiss](../../events/switzerland/swiss_neutrality.txt) periodic events apply separate national modifiers.

[Decolonization](../../common/journal_entries/ztr_je_decolonization.txt) begins through the world technology/pressure chain. [Effects](../../common/scripted_effects/ztr_decolonization_script.txt) and [decisions](../../common/decisions/ztr_decolonization_decisions.txt) connect pressure, petitions, independence, claims and homeland transfers.

## Limits and editing

Removed EU gameplay has not been restored. [Superstate country definitions](../../common/country_definitions/ztr_superstates.txt) explicitly describe unreachable future formations; the [continental-confederation identity](../../common/power_bloc_identities/ztr_power_bloc_identities.txt) is hidden.

Preserve event IDs, scopes and shared vote state. Check the individual [game-rule](../../common/game_rules/ztr_game_rules.txt) conditions instead of assuming every national event shares a gate. These systems were inspected, not played through. Follow [editing and verification](../development/editing-and-verification.md) and [military/nuclear guidance](military-and-nuclear.md).

## Performance implementation, 2026-11-10

UN comparisons prepare country data once for both laws, then clear it after the pair. The law-specific scoring body, per-law result/role resets and final decisions remain in place. `ztr_un_value_law` is still the complete public single-law effect. Internal paired callers use `ztr_un_value_law_from_prepared_context` and finish with `ztr_un_value_law_clear_country_context`. The retry budget, random selection, vote timing and proposer search are unchanged; no proposer cache or saved-data migration was added. See [the implementation record](../../milestones/behavior-preserving-performance/info.md).
