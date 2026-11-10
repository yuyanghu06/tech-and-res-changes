# Focused source checks

Run `python -B -m unittest discover -s tests -v` from the repository root. The checks use only Python's standard library and Git; they do not open the game or change launcher settings.

The tests read the actual city scripts, follow their technology checks, and choose the highest-weight matching city. They cover every technology stage, socialist and other governments, the Russian pack enabled or disabled, and regions outside its coverage. They check custom model proportions, removed Eastern European test overrides, preserved African and production definitions, and city-centerpiece links and building requirements.

Preservation checks compare against the imported source commit `38b0685472188a42ca7dee4adb047b6a0b4c61f6`, named once as `IMPORTED_BASELINE_COMMIT` in the test file. This fixed reference keeps those checks valid after the fix is committed. The checkout must retain that Git commit.

This is a small evaluator of the relevant script conditions, not the game engine. Native Russian coverage is supplied as an input; verifying its region list and checking model/entity definitions against installed game files are separate local checks. These tests do not prove map appearance or whether the game refreshes an existing city after research.

## Gameplay-preserving performance checks

`test_performance_optimizations.py` adds eight tests comparing actual parsed scripts against the same fixed imported commit. The complete suite now has fourteen tests. It checks environmental support and explanation entries, research cap values, both nuclear programs' paused/running progress and limits, nuclear attack exclusions/strength, and UN pair/single-law cleanup and decisions.

The tests cover 929 paired fixtures using Decimal arithmetic and explicit country/state/population inputs. They count evaluations to confirm duplicate work is removed. UN orchestration uses deterministic preparation/scoring boundaries; separate exact syntax-tree comparisons establish that the real scoring, preparation and selectors are preserved. Unsupported evaluator operations raise errors.

This is a bounded source evaluator, not the game engine or a timing benchmark. It does not prove engine fixed-point details, rendered tooltips, save loading or campaign outcomes. [The implementation record](../milestones/behavior-preserving-performance/info.md) tracks independent review and runtime limits. Run the same discovery command above for all fourteen tests.
