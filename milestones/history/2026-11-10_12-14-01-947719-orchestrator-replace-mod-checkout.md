# Replace old local mods with the Git checkout

- Local timestamp / acting role / milestone: 2026-11-10 12:14:01.947719 -05:00 America/New_York / orchestrator / russian-city-appearance
- Requested scope: Remove old Tech & Res directories, clone the supplied source directly as a new mod, and configure its remote.
- Starting repository state: Five verified old directories existed; source main resolved to 38b0685472188a42ca7dee4adb047b6a0b4c61f6.
- Work performed / changed files: Moved tech&res_updated, tech&res_model_units, my tech&res tweaks, tech & res + more resources patch, and muc_tnr_compatch_updated to Windows Recycle Bin; cloned tech-and-res-changes.
- Decisions: Automatic review blocked the permanent-delete command before execution; used recoverable Recycle Bin removal instead. No launcher/database/playset edits.
- Checks and evidence: All targets resolved under the mod directory and contained no reparse points; removal verified per path. Clone exited 0; clean main tracks origin/main; origin fetch/push URL is the requested GitHub repository.
- Resulting state / acceptance: Import complete. Unrelated folders remained outside the removal list.
- Remaining work and handoff: Research and fix the newly requested Russian city appearance problems.
