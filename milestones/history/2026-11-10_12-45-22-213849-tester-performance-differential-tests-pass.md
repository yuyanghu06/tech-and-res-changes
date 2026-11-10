# Pass original/current calculation checks

- Local timestamp / acting role / milestone: 2026-11-10T12:45:22.213849-05:00 / Tester / behavior-preserving-performance.
- Requested scope: as many performance changes as possible while preserving the existing game.
- Starting repository state: five local cleanups implemented; earlier city/thumbnail/docs changes retained; independent validation pending.
- Work performed / changed files: Tester added only tests/test_performance_optimizations.py. Eight new tests execute parsed source with Decimal fixtures; original/current results match 929 paired cases. UN orchestration uses disclosed deterministic boundaries plus exact real scoring/preparation preservation. Only Orchestrator writes shared journal files.
- Decisions: retain all gameplay rules, update dates, random choices, UN retry budget, public scorer and variable cleanup; no persistent caches/migration or demographic/AI changes.
- Checks and evidence: 14 tests pass, including 929 paired cases; actual evaluation counts confirm work removed. Five scripts preserve BOM/CRLF and unique balanced definitions; unaffected definitions/cadences/random tokens preserved; exact UN scoring/preparation retained; diff and document checks pass. These are source/Python checks, not engine tests.
- Resulting state / acceptance: PASS. Full suite: 14/14 tests; git diff --check passed. No production correction needed.
- Remaining work and handoff: no required code fixes remain. A future controlled game check must establish copied-save loading, rendered breakdowns and actual speed; prior Russian city appearance remains separately unverified.
