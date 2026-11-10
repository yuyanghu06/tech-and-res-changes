# Late-game performance investigation

Investigated November 10, 2026, against local Tech & Res commit `38b06854` with the existing uncommitted Russian city fixes preserved, and installed Victoria 3 version 1.15.0. This was a source investigation. No gameplay code, game settings, saves or launcher state were changed. No simulation timing was captured.

There are concrete opportunities to remove repeated work. Start with calculations that can reuse the same result during one update. Changing how often countries make decisions or changing population identities is a separate gameplay choice. The priorities below reflect where work repeats and how broadly it can apply, not measured speed rankings.

## Recommended first changes

### 1. Calculate environmental support's state pollution value once

`common/political_movements/ztrpol_movements.txt:194` calculates a state's pollution per million people to test a threshold. Line 197 calculates it again for the support multiplier when the threshold is exceeded. This is inside `pop_support_weight`, the formula used to decide a population group's support.

The formula at `common/script_values/ztrpol_movement_values.txt:54` reads state pollution and population and calls the country's environmental reductions. Those reductions, starting at line 5, check laws, institution investment and technology. The installed game's `common/script_values/script_values.md:19` explicitly says formula values are recalculated every time they are evaluated. Merely giving a formula a name does not save its result.

**Proposed change:** calculate the state value once within this support evaluation and reuse a temporary value. Installed vanilla script values use `save_temporary_value_as`, for example `common/script_values/ai_script_values.txt:179`. Preserve the threshold, multiplier, rounding and displayed explanation.

**Why this could matter late in a campaign:** the formula is evaluated for separate population groups. More groups create more opportunities for repeated work. Actual call frequency and time must be captured in the game; this is not an explicit monthly callback.

**Boundary:** sharing one saved result across every group in a state could remove more work, but retaining that result between dates introduces delayed responses to changes in pollution, population, policies or ownership. Do not add a monthly or yearly cache as part of the exact local cleanup. The country-wide counterpart at `ztrpol_movement_values.txt:66` also sums states for movement creation and is another profiling target. Both mod files identify absent generators, so any future direct edit must be recorded.

### 2. Prepare UN country data once when comparing two laws

`common/scripted_effects/ztr_un_law_opinion_functions.txt:705` and line 713 score the current and possible law. Neutral voter comparisons repeat the same pattern at lines 780 and 787. Each score calls `ztr_un_value_law_prepare_country_context` at line 1562.

That preparation, starting at line 846, recalculates liberty/equality and rebuilds the country's literacy, development, demography, government and economic balances. It does not read the considered law or subject. Both laws in a comparison use the same country inputs.

**Proposed change:** prepare country data once for the pair, then score both laws from it. Keep a complete entry point for callers that score only one law. Preserve all law-dependent calculations, temporary-variable cleanup and vote decisions. Compare exact scores before accepting the refactor; the function's size alone is not a timing measurement.

There is another repeated world search during voting: line 4855 scans countries to find the proposal's author while scoring each voter. `common/scripted_effects/ztr_un_scripts.txt:263` updates neutral voters, called immediately and monthly by `common/journal_entries/ztr_je_un.txt:201`. Retaining the author's country reference when a vote starts could remove these repeated searches. It requires checking all proposer assignment and cleanup paths before implementation.

### 3. Skip unused calculations for paused nuclear research

`common/scripted_effects/ztr_technology_scripts.txt:142` and line 195 calculate progress using research capacity, agreements, rival pressure and technologies, then multiply the gain by zero if nuclear research is paused. Their monthly callers are `common/journal_entries/ztr_je_atomic.txt:27` and line 160.

**Proposed change:** check the pause before computing the unused gain. Keep the existing goal checks, 80% limits and subsequent clamps. This is a smaller, situational saving that applies only while a program is paused.

### 4. Remove one duplicate treaty traversal from a research tooltip

`common/script_values/ztr_research_values.txt:217` calculates agreement points lost to the cap as raw points minus capped points. Capped points, at line 211, calculate raw points again, so the treaty/article traversal at line 175 runs twice.

**Proposed change:** calculate raw points minus the cap and floor the result at zero. In this script language, `max` applies an upper limit and `min` applies a lower limit, so the equivalent formula is:

```text
value = ztr_research_agreements_raw
subtract = ztr_research_agreements_cap
min = 0
```

This is an exact local simplification, chiefly for the Research Center breakdown (`common/scripted_guis/ztr_journal_entry_sguis.txt:293`). The algebra was checked for 21 Decimal cases below, at and above the cap. It is not a major simulation-speed claim.

## Larger opportunities that change behavior unless handled carefully

### UN proposal retries increase with membership

The UN information journal explicitly uses `context = country` (`common/journal_entries/ztr_je_un.txt:4`). Its annual proposal coordinator at line 46 can choose up to two AI permanent members using world searches, choose a proposal and score it. Failed attempts release the temporary lock at line 108 without recording an annual attempt or cooldown. Other member journals can therefore try again. Success sets the global vote-in-progress flag (`common/scripted_effects/ztr_un_scripts.txt:449`) and stops subsequent attempts while voting is active.

One global coordinator would avoid repeated failed attempts as membership grows. However, fewer attempts mean fewer chances to find an acceptable proposal. This needs a decision about intended proposal frequency, or an equivalent attempt budget that preserves the current behavior. It is not a free change to update frequency.

### Population consolidation is a gameplay option

The mod's Population Lag Fix defaults off (`common/game_rules/ztr_game_rules.txt:23`). If enabled, its events are considered monthly through `common/on_actions/ztr_on_actions.txt:682`. The guards prevent population loops when the rule is disabled.

`events/yeet_pops.txt` traverses population groups separately for culture and religion: lines 46 and 94 in low mode, lines 151 and 176 in the more aggressive mode. Eligible groups are converted to the country's primary culture and state religion. This can reduce the number of distinct groups, but it changes demographics. Combining the passes also needs care because changing culture can affect acceptance and grouping before religion processing.

Installed vanilla already has population merging and a Moderate/Aggressive consolidation rule (`game/common/game_rules/00_game_rules.txt:120`). Its defines at `game/common/defines/00_defines.txt:1688` include thresholds that respond to the number of population objects. Version 1.15 also dissolves very small groups into same-culture, same-religion groups at line 1715. Tech & Res does not override these settings. Test the existing options separately before considering new population changes.

### Slower AI updates have a cost

Installed `game/common/defines/00_ai.txt:6` refreshes full spending variables every 100 ticks; building spending-state refresh is spread across 100–200 ticks at lines 10–13. Raising those intervals might save work while delaying AI reactions to economic changes. Tech & Res does not override them. Measure the script cleanups first.

## Work that is already bounded

- **Climate:** `je_group_global_warming` has `context = none` (`common/journal_entry_groups/ztr_journal_entry_groups.txt:41`). Its journal runs globally, even though countries are involved in it. The yearly pollution recount is not repeated for every country. Installed `common/journal_entries/journal_entries.md:11` documents context inheritance. Do not propose fixing nonexistent per-country duplication.
- **Demography:** yearly per populated country, with an elapsed-year guard, national totals and five stored history samples (`common/on_actions/ztr_demography_on_actions.txt:18`; `common/scripted_effects/ztr_demography_scripts.txt:179`). It does not explicitly traverse every population group. A duplicated bar update is minor.
- **Airports:** yearly per state and on state creation; the modifier changes only when capacity changes (`common/scripted_effects/ztr_airport_effects.txt:1`).
- **Resources:** new deposits use technology acquisition and global one-time flags (`common/on_actions/ztr_on_actions.txt:740`). They are not recurring full-map creation scans.
- **Nuclear rankings and ideological poles:** already use stored values and annual updates. Early exclusions before nuclear building scans are a lower-priority candidate (`common/script_values/ztr_nuclear_values.txt:18`, exclusions at line 105).
- **Research agreement AI:** the separate diplomatic-action file is entirely commented out. There are not two live proposal channels. The active treaty already uses `inherent_accept_score`, the intended lower-refresh scoring location. Some comments still describe the disabled channel.
- **UN display lists:** existence checks followed by another country scan appear at `common/scripted_guis/ztr_journal_entry_sguis.txt:152` and subsequent vote lists. These are display/tooltip work. Profile the journal open and closed before prioritizing them as a cause of simulation lag.

The mod's explicit recurring hooks are mainly monthly and yearly. Engine-controlled formulas and interface requests are a separate source of work, so counting pulse hooks or file length alone cannot establish a bottleneck.

## How to establish an actual speed improvement

1. Use a copied late-game save and the same game version, mods, rule settings, speed and camera position. First measure with journals closed. Keep autosave behavior identical and distinguish saving time from simulation time.
2. Warm up the simulation, then measure the same fixed date interval several times. Include normal weeks, month boundaries and a year boundary. Record median elapsed time and visible pauses separately from frame rate.
3. The installed interface contains `Script.Profiling.Gui` (`game/gui/console.gui:560`) and `TickTask.List` (`game/gui/error_deer.gui:141`). The bundled script profiler has capture controls, tick counts, per-file times and call counts; the tick-task debugger shows task frequency and average times. Their presence is confirmed from local files; opening and using them in this release has not been tested.
4. Capture baseline call counts and timings, then change one candidate at a time. Reuse the same copied save for each run. Measure ordinary speed without profiling too, because capture adds overhead.
5. For exact cleanups, compare the affected values at the same starting state: political support and tooltip text, UN scores and vote choices, paused/resumed nuclear progress and caps, and research agreement cap display. Check broader campaign outcomes for unintended changes. A long simulation can diverge for unrelated reasons, so a changed final GDP alone is not proof that a local formula changed.

Start with environmental support and UN score preparation. These have clear repeated work and can be changed without intentionally slowing a feature's response. Test paused nuclear arithmetic and the tooltip simplification as smaller follow-ups. Revisit update intervals or demographic changes only if the measured remaining cost justifies the gameplay tradeoff.

## Evidence and limits

Three read-only Researchers examined gameplay scripts, research/politics and installed engine settings. A separate Tester pass cross-checked scheduling, formula reevaluation, population-rule effects and climate context. The assembled report received source-audit PASS with no required corrections and an independent Evaluator ACCEPT for investigation only. Existing city tests passed (six tests); `git diff --check` passed. Those checks preserve prior work; they do not benchmark performance.

Paradox's [performance developer diary](https://www.paradoxinteractive.com/games/victoria-3/news/dev-diary-76-performance) explains the difference between simulation time and frame rate, the effect of separate population groups, and why repeated modifier work matters. It dates to 2023 and supports the general reasoning, not numerical claims for this 1.15 mod. Current recommendations use installed 1.15 scripts and documentation.

An engine-hook project, [Vic3 Performance Hooks](https://github.com/CrimsonBolt/Vic3-Performance-Hooks), was inspected as a separate approach. The Researcher found a recent November 6, 2026 commit, an MIT license, vendored MinHook under BSD-2-Clause and a CMake/C/C++ build. Its documentation describes skipped engine updates, altered AI/world development and possible injection deadlocks; Tech & Res compatibility was not established. No code was copied or installed. Executable patching is outside this mod-script investigation, and its published speed claims do not predict this mod's gains.

No optimized scripts have been implemented, no game session was launched and no speedup percentage can be supported yet. The requested investigation can be completed from this evidence; performance acceptance belongs to a subsequent measured implementation.
