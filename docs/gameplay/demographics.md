# Demographics, education and population

The mod tracks a country's demographic transition and uses its current stage to change population-related modifiers. This is separate from the game's actual population simulation. A progress score, displayed stage and estimated birth/death figures are different things; changing a displayed estimate does not necessarily change population growth.

## Stored progress and yearly changes

[Demographic effects](../../common/scripted_effects/ztr_demography_scripts.txt) own the saved country variables. ztr_demography_initialize creates missing progress and history, adds je_demography where necessary and refreshes its bar. Initialization uses living standards and historical/regional exceptions, including different starting treatment for France, Britain, Spain, sub-Saharan Africa and South/Southeast Asia.

[Demographic values](../../common/script_values/ztr_demography_values.txt) calculate changes from literacy, living standards, calendar time and economic change, with additional healthcare, slavery, social, regional and immigration terms. Progress stays between 0 and 1000. It is translated into nine displayed stages. Do not replace this with the older comments that describe stages as living-standard thresholds alone.

The country keeps five years of living-standard and per-person economic observations. The economic contribution waits for enough recorded history. Yearly updates avoid applying twice in the same year and fill skipped observations according to the script. The effects save the contribution breakdown before changing progress, so the journal describes that update rather than a newly recalculated result.

[The demographic journal](../../common/journal_entries/ztr_je_population.txt) displays progress and applies the matching demographic_stage_N modifier. It also applies calendar-based medicine modifiers. [Population modifiers](../../common/static_modifiers/ztr_population_modifiers.txt) affect birth rates, mortality, the working-adult share and, in some stages, school costs. Changing a formula without reviewing those modifiers can produce a different population result than intended.

## New countries and political disruption

[Demographic hooks](../../common/on_actions/ztr_demography_on_actions.txt) initialize untracked countries monthly and update countries yearly. They also handle revolutions, secessions and released countries. A revolution inherits its parent's progress and history; secessions initialize their own history, and release hooks initialize the new country. The main [periodic hook file](../../common/on_actions/ztr_on_actions.txt) registers the monthly/yearly calls.

Preserve both the variable state and the journal connection. Editing only the progress bar leaves the actual demographic stage unchanged.

## Migration, education and other population changes

[Social conditions](../../common/scripted_triggers/ztr_demography_triggers.txt) read healthcare and slavery laws, specified religious/caste conditions, and openness to immigration. The immigration contribution adjusts demographic progress; it does not itself move individual populations between countries.

The vital-rate values near the end of [ztr_demography_values.txt](../../common/script_values/ztr_demography_values.txt) explicitly serve the population-growth tooltip. They estimate births and deaths from the engine's net growth. These estimates are not separately saved or advanced by a periodic update.

[Advanced education laws](../../common/laws/ztr_advanced_education.txt), healthcare laws and urban healthcare production methods connect population behavior to [politics](politics-and-laws.md). Country-specific events also apply modifiers: [France](../../events/france/france_pop.txt), [German countries](../../events/germany/germany_pop.txt), [Brazil](../../events/brazil/brazil_pop.txt) and [colonial/subject population booms](../../events/decolonization/colony_pop.txt). Their conditions and player/AI effects differ; do not assume one shared historical-content switch covers every event.

The optional [population performance events](../../events/yeet_pops.txt) change eligible populations' cultures and religions. The [game-rule file](../../common/game_rules/ztr_game_rules.txt) defaults that feature to off. It is a separate population-changing feature, not part of demographic progress.

## Editing and verification

Keep saved-variable names and revolution/release handling consistent with the journal, modifiers, messages and [English demographic text](../../localization/english/ztr_demography_l_english.yml). The current focused tests check city graphics, not demographic outcomes. Read [editing and verification](../development/editing-and-verification.md); test initialization, a yearly update and a newly separated country in game before claiming population behavior works.
