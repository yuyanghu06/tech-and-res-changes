# Scripted effects

These helpers change country, state and global data. Find the active caller, its scope and cleanup before editing a shared effect. Start with [startup and periodic work](../../docs/architecture/startup-and-periodic-work.md) and the relevant [gameplay guide](../../docs/gameplay/info.md).

The performance changes are local to two files:

- `ztr_un_law_opinion_functions.txt`: `ztr_un_value_law` remains the complete single-law entry point. Paired comparisons prepare country inputs once, use `ztr_un_value_law_from_prepared_context` for each law, then call `ztr_un_value_law_clear_country_context`. The prepared scorer still resets results and clears its law-specific role each time. Do not call it without preparation and eventual cleanup.
- `ztr_technology_scripts.txt`: paused nuclear and thermonuclear programs add zero without calculating an unused research gain. The existing goal gates and later progress clamps still run in their original positions.

No update dates, UN proposal attempts, random choices or saved identifiers were changed. See [the performance implementation](../../milestones/behavior-preserving-performance/info.md) for evidence and runtime limits.
