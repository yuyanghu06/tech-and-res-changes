# Project notes

## 2026-11-10

- Imported `https://github.com/yuyanghu06/tech-and-res-changes.git` into this new mod folder. `origin` points there; `main` tracks `origin/main`. Imported commit: `38b0685472188a42ca7dee4adb047b6a0b4c61f6`.
- Removed five previous Tech & Res folders from the parent `mod` directory by moving them to the Windows Recycle Bin: `tech&res_updated`, `tech&res_model_units`, `my tech&res tweaks`, `tech & res + more resources patch`, and `muc_tnr_compatch_updated`.
- Requested fixes: prevent modern Russian/Eastern European test buildings from appearing before their technology, and use the Russian building pack in the cities where the pack applies.
- Researchers found eight temporary Eastern European city overrides with state-only checks and weight 1000. Normal production rules already have technology checks. The temporary overrides bypass them.
- The Russian pack belongs to game DLC `dlc019_ip5`; selection requires `ip5_cosmetics` and the native `russian_buildings_trigger`.
- `AGENTS.md` did not exist in the incoming checkout. Shared role files and `AGENT_WORKFLOW.md` were also unavailable locally. Repository instructions were written from local inspection and two independent research reports.
- Current work and verification are recorded in [the milestone snapshot](milestones/milestone.md).
- Implemented the scoped fix: removed eight forced Eastern European test cities and matching centerpieces; added ten Russian city variants with the existing technology checks, native Russian DLC/geography checks, and preserved custom modern models. Skyscraper centerpieces require a building under construction or with a completed level.
- Six independent source tests pass; 91 referenced model/entity names resolve in local assets. Final independent review: ACCEPT for code and static checks. No in-game visual check has been performed, and launcher playsets were not changed.
- Run focused checks with `python -B -m unittest discover -s tests -v` and `git diff --check`. Preservation tests compare with the fixed imported commit so later commits do not change the baseline.

- Launcher thumbnail: copied the existing artwork to .metadata/thumbnail.png; the user confirmed the preview works. Identity metadata and root artwork were preserved.
- Follow-up request: even out AGENTS.md across the entire mod and create organized docs explaining current features/source structure. Thumbnail took priority and is complete; documentation research has resumed. Preserve the separate performance investigation recorded in project milestones.
- Completed the documentation request: balanced AGENTS.md, fifteen source-backed topic guides under docs/architecture, docs/gameplay, docs/visuals and docs/development, linked indexes and source-folder info.md guides. Removed the docs ignore rule so the guides can be committed.
- Documentation checks passed: all local links resolved, text/whitespace checks passed, and both cross-author reviews returned ACCEPT. Current features, inactive/TODO material, absent generators and runtime evidence limits are explained separately. These docs do not claim whole-mod gameplay verification.

- Requested a late-game performance investigation. [Findings and measurement plan](milestones/late-game-performance/report.md) identify repeated political pollution calculations, UN law preparation, paused nuclear arithmetic and a duplicate research tooltip traversal. Investigation only; no gameplay code changed and no speedup measured.
- Performance investigation completed: independent source Tester PASS and Evaluator ACCEPT. No performance improvement is claimed until controlled in-game measurement exists.

- User authorized as many performance changes as possible while preserving the existing game. Implement only local repeated-work cleanup; no demographic conversion, slower AI, fewer UN attempts, saved-state migration or changes to update dates. [Implementation record](milestones/behavior-preserving-performance/info.md).

- Implemented the five gameplay-preserving performance cleanups. Independent Tester PASS and Evaluator ACCEPT for code/source checks; fourteen tests pass, including 929 paired cases. Saves, rules, update timing, random choices and prior city/thumbnail work were not changed. In-game loading/tooltips/speed remain unverified. [Changes and evidence](milestones/behavior-preserving-performance/changes.md).

- User requested push. Publishing the tested local state: performance cleanups, prior reviewed Russian city fixes, launcher thumbnail and repository guides. [Publication record](milestones/publish-reviewed-updates/info.md).

- Published reviewed implementation, prior city fixes, thumbnail and guides to origin/main in `2ceab5fd91b85ce3fe4ec15e73a3d7ebc5cff1ae`. Remote commit matched local HEAD and tree was clean before the documentation-only publication record. All14 tests passed before publication; runtime limits are unchanged.
