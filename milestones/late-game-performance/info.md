# Late-game performance investigation

- Goal: identify concrete ways to reduce recurring simulation work in Tech & Res, especially late in a campaign.
- Scope: inspect mod scripts, their callers and update frequency; compare installed game definitions read-only; research primary sources; independently check the findings. This request is an investigation, not approval to change gameplay.
- Completion criteria: ranked findings with source locations, actual call frequency, behavior tradeoffs, evidence limits, and a repeatable before/after measurement plan; independent review of the report.
- Status: completed investigation. Independent source Tester PASS and Evaluator ACCEPT; no required report corrections. No gameplay optimization or runtime measurement performed. Shared role files and AGENT_WORKFLOW.md remain unavailable; specialists received explicit role boundaries.
- Boundaries: preserve existing uncommitted Russian city work. Do not change gameplay scripts, installed game files, other mods, saves, launcher/playset state or running apps.
- Report: [ranked findings, behavior tradeoffs and measurement plan](report.md).

- Verification: source citations and scheduling independently checked; 21 Decimal cap-equivalence cases passed; six existing city tests passed; git diff --check passed. These do not establish an in-game speed gain.
- Next action: for a later implementation request, measure a copied late-game save before and after each proposed change. Prior Russian city visual acceptance remains open.
