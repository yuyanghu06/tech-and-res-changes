# Tech & Res

This folder is the installed full mod and its Git checkout. Game content is under `common`, `events`, `gfx`, `gui`, `localization`, `dlc` and `dlc_metadata`. The launcher reads `.metadata/metadata.json`.

Read [AGENTS.md](AGENTS.md) for the structure and editing rules, [notes.md](notes.md) for dated user notes, and [milestones/milestone.md](milestones/milestone.md) for the current work and checks.

[The documentation index](docs/info.md) links the full architecture, current gameplay features, visuals, localization and editing guides. [Feature status](docs/development/feature-status.md) distinguishes active source from inactive plans and actual runtime evidence. The launcher thumbnail is user-confirmed; the other gameplay systems have source guidance rather than a claim of whole-mod runtime verification.

[tests/info.md](tests/info.md) explains the six focused city selection checks and how to run them. They check source conditions and references; the game appearance still needs observation.

[Late-game performance investigation](milestones/late-game-performance/report.md) records source-backed optimization candidates, gameplay tradeoffs and the measurement needed before claiming gains.

[Gameplay-preserving performance changes](milestones/behavior-preserving-performance/info.md) implement the local calculation cleanups authorized after the audit; update timing, demographics and saved campaign data are preserved in the source plan. Runtime checks remain separate.
