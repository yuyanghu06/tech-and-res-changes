# Research native Russian city pack rules

- Local timestamp / acting role / milestone: 2026-11-10 12:14:01.959504 -05:00 America/New_York / researcher / russian-city-appearance
- Requested scope: Identify supported conditions and model mappings from the installed game.
- Starting repository state: Source production city pools use European historical assets; Russian pack behavior needed verification.
- Work performed / changed files: Second independent read-only researcher inspected installed Victoria 3 city examples, common/scripted_triggers/00_gfx_buildings_graphics_triggers.txt and dlc/dlc019_ip5/gfx/map/city_data.
- Decisions: Use separate city-only Russian variants guarded by ip5_cosmetics and russian_buildings_trigger, with original technology/socialist checks and weight +3. Preserve custom models and skyscraper building requirements.
- Checks and evidence: Native Russian pack and geography names verified; native comments establish state-region scope and higher-weight priority. Native city types provide no inheritance pattern; TRY_INJECT only appends entries in inspected examples.
- Resulting state / acceptance: Focused implementation plan supported by installed primary source files. No copied Workshop code or external dependencies needed.
- Remaining work and handoff: Implement separate Russian city variants and matching centerpieces; static and game checks follow.
