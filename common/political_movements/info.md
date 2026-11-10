# Political movements

These files define movement availability and the formulas for population support. Read [politics and laws](../../docs/gameplay/politics-and-laws.md) and follow each value to `common/script_values` before editing it.

The environmental movement in `ztrpol_movements.txt` reuses pollution within a single support evaluation. It saves and restores the accumulated support while calculating that input; the temporary values are not stored campaign variables. The existing threshold, multiplier and description remain in place.

The file names an absent politics generator. The performance change is a focused direct edit; no regeneration command is available. See [the performance implementation](../../milestones/behavior-preserving-performance/info.md) for checks and runtime limits.
