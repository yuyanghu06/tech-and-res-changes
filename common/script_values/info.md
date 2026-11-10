# Script values

These formulas calculate numbers for gameplay and displays. Named formulas run when evaluated; a name alone does not save a result for reuse. Read the relevant [gameplay guide](../../docs/gameplay/info.md) and trace callers before changing an expression.

- `ztr_research_values.txt` supplies research capacity and treaty contributions. The over-cap display subtracts the cap once and applies a zero floor; actual agreement contributions are unchanged.
- `ztr_nuclear_values.txt` supplies silo strength and attack/defence values. Countries already excluded by capability, uranium law or subject status skip attack calculations. Eligible countries retain the original arithmetic and operational-silo check. Defence is unchanged.
- `ztrpol_movement_values.txt` supplies live pollution formulas used by political support; no result is retained between dates by the performance changes.

See [the performance implementation](../../milestones/behavior-preserving-performance/info.md). Source tests do not establish the game engine's runtime behavior or a speed gain.
