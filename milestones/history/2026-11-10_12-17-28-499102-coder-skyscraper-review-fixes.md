# Tighten skyscraper requirements and match native attachments

- Local timestamp / acting role / milestone: 2026-11-10 12:17:28.499102 -05:00 America/New_York / coder / russian-city-appearance
- Requested scope: correct root/Tester findings in the new Russian centerpiece file only.
- Starting repository state: first implementation copied an optional building scope check and grouped two native Russian models as alternatives in one attachment.
- Work performed / changed files: updated only gfx/map/city_data/city_centerpiece/ztr_eeu_russian_cities.txt. All five skyscraper triggers now use any_scope_state / any_scope_building with building_skyscraper type and construction-or-positive-level checks. The early Russian skyscraper has two separate attach blocks.
- Decisions: require a real matching building; preserve construction behavior. Match native Russian attachment structure. Do not change old regional centerpiece files.
- Checks and evidence: syntax matches installed game/events/belle_epoque_events.txt:135-139, common/scripted_triggers/00_building_triggers.txt:12-14 and gfx/map/city_data/city_centerpiece/cities.txt:41. Russian attachment reference is dlc/dlc019_ip5/gfx/map/city_data/city_centerpiece/russian_centerpieces.txt. Coder brace/assert checks and git diff --check passed; root inspected corrected source.
- Resulting state / acceptance: requested code corrections complete; independent tests and review pending. No in-game observation.
- Remaining work and handoff: Tester runs focused source selection/building tests; Evaluator reviews final code and evidence. Keep visual milestone open until game observation.
