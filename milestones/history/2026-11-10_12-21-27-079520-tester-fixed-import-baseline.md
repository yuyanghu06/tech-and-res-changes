# Keep preservation tests stable after commits

- Local timestamp / acting role / milestone: 2026-11-10 12:21:27.079520 -05:00 America/New_York / tester / russian-city-appearance
- Requested scope: Correct only the regression-test baseline and its guide.
- Starting repository state: Six tests passed, but two preservation comparisons read moving HEAD.
- Work performed / changed files: Added IMPORTED_BASELINE_COMMIT = 38b0685472188a42ca7dee4adb047b6a0b4c61f6 and used it at both git-show comparison sites in tests/test_russian_city_graphics.py; documented the fixed baseline in tests/info.md.
- Decisions: Use immutable imported source for before-state comparisons; no production edits or commits.
- Checks and evidence: All six focused tests passed again; git diff --check passed.
- Resulting state / acceptance: Test-maintenance finding resolved.
- Remaining work and handoff: Evaluator rechecks correction and reaffirms final decision.
