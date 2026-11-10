# Implemented performance changes

The user authorized changes that preserve the existing campaign. These edits remove repeated or unused calculations; they do not change update dates, laws, population identities, AI reaction intervals, UN attempt counts or random choices. No save, playset, launcher setting or installed game file was edited.

| Area | Work removed | Behavior retained |
| --- | --- | --- |
| Environmental movement | Second pollution calculation for qualifying population support | Same accumulated support, pollution threshold, multiplier, policy inputs and description; temporary values are reused only within that evaluation |
| UN law comparisons | Second preparation of country inputs within a two-law comparison | Original law scoring, role/result resets, cleanup, proposal/voter decisions and complete public single-law function |
| Paused nuclear programs | Research, treaty and rival arithmetic whose gain would be zeroed | Same monthly updates, accumulated progress, goal gates, 80% limits and subsequent clamps |
| Research cap display | Second traversal of research agreements | Same points lost above the cap, including fractional values |
| Nuclear attack strength | Building scans and arithmetic for countries already excluded by capability, law or subject status | Zero for excluded countries; original eligible-country arithmetic and operational-silo exclusion; defence untouched |

The environmental movement file is generated output whose generator is absent. Its edit is narrow and direct. All five gameplay files retain UTF-8 BOM and CRLF. No new persistent country/state variables or migration are introduced. Public scripted-effect names are preserved; two internal UN helpers are added.

Verification complete for code/source acceptance:

- All fourteen tests pass: six prior city tests and eight new performance tests.
- The new tests compare actual original/current scripts across 929 paired fixtures: environmental support/explanation entries (84), research caps (18), nuclear progress (384), nuclear attack strength (192), UN proposal comparisons (104), neutral-voter decisions (144) and public single-law calls (3).
- Evaluation counts confirm one pollution calculation, one raw agreement traversal, no unused paused research-capacity calculation, no excluded-country attack building scan and one UN preparation per pair.
- The real UN scoring, preparation and selectors are preserved by exact syntax-tree checks. Orchestration fixtures use documented deterministic preparation/scoring boundaries; they do not execute every real UN score in the engine.
- Five gameplay scripts have balanced, unique definitions and retain UTF-8 BOM/CRLF. Unaffected definitions, random calls and update timing are unchanged. `git diff --check` and documentation-link checks pass.
- Independent Tester PASS and Evaluator ACCEPT for code/source checks. No production fixes were required after testing.

Tests use the fixed imported source commit `38b0685472188a42ca7dee4adb047b6a0b4c61f6` as their baseline. They do not benchmark the engine or model its fixed-point arithmetic exactly.

These checks are not an in-game save-load or tooltip-rendering test. No speedup has been measured. The original [audit](../late-game-performance/report.md) remains the record of the investigation before implementation.
