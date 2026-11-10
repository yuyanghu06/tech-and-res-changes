# Start gameplay-preserving performance work

- Local timestamp / acting role / milestone: 2026-11-10T12:38:17.956663-05:00 / Orchestrator / behavior-preserving-performance.
- Requested scope: make as many optimizations as possible without affecting the existing game.
- Starting repository state: imported 38b06854 plus existing city, thumbnail and documentation changes; investigation source report accepted. Shared role files/workflow remain unavailable, so explicit role boundaries apply.
- Work performed / changed files: Read current AGENTS.md and system guides; confirmed existing local city/thumbnail/docs changes. User authorized behavior-preserving implementation; assigned exclusive ownership without changing saves or settings. Initialized milestones/behavior-preserving-performance/info.md and updated tracking.
- Decisions: only within-evaluation reuse and early rejection of already-discarded calculations; no saved-state migration or gameplay/timing changes.
- Checks and evidence: prior source investigation and fresh call-site/encoding inspection; independent test plan uses actual baseline/current script expressions and fails unsupported syntax.
- Resulting state / acceptance: Scope accepted; no update timing, demographics, random choices or persistent campaign data may change.
- Remaining work and handoff: implement within owned files, independently test/evaluate, fix findings and record limits; retain prior city runtime checks.
