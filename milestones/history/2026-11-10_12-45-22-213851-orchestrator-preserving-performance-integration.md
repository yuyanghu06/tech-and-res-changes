# Integrate accepted calculation cleanups

- Local timestamp / acting role / milestone: 2026-11-10T12:45:22.213851-05:00 / Orchestrator / behavior-preserving-performance.
- Requested scope: as many performance changes as possible while preserving the existing game.
- Starting repository state: five local cleanups implemented; earlier city/thumbnail/docs changes retained; independent validation pending.
- Work performed / changed files: Integrated five local cleanups, independent tests and affected system/folder guides. Refreshed test instructions, notes, milestone snapshot/work list and changes/evidence. Existing city, launcher thumbnail and other documentation work retained. Only Orchestrator writes shared journal files.
- Decisions: retain all gameplay rules, update dates, random choices, UN retry budget, public scorer and variable cleanup; no persistent caches/migration or demographic/AI changes.
- Checks and evidence: 14 tests pass, including 929 paired cases; actual evaluation counts confirm work removed. Five scripts preserve BOM/CRLF and unique balanced definitions; unaffected definitions/cadences/random tokens preserved; exact UN scoring/preparation retained; diff and document checks pass. These are source/Python checks, not engine tests.
- Resulting state / acceptance: Implementation and source acceptance complete, with no required fixes. No commit/push, game launch, save change or speed claim.
- Remaining work and handoff: no required code fixes remain. A future controlled game check must establish copied-save loading, rendered breakdowns and actual speed; prior Russian city appearance remains separately unverified.
