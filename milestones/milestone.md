# Current milestone

- Goal: reduce repeated calculations without changing existing campaign rules, results, random choices, update dates or stored data.
- Active milestone: [gameplay-preserving performance](behavior-preserving-performance/info.md), implementation complete and independently accepted for code/source checks. The [performance audit](late-game-performance/info.md) is complete; prior city visual checks remain open and separate documentation work is preserved.
- Implemented state: five local cleanups in political support, UN law comparisons, paused nuclear research, research cap display and nuclear attack exclusions. Affected system/folder guides updated. Prior Russian city fixes and launcher thumbnail preserved.
- Decisions: reuse values only within one evaluation; keep public single-law scoring complete and all cleanup intact. No demographic conversion, fewer UN attempts, persistent proposer cache, AI/pulse changes, balance edits or save migration.
- Boundaries: only the five owned gameplay files plus focused tests and repository documentation. Installed game files are read-only. Saves, running apps, launcher state, playsets, sibling mods and personal settings remain outside this work.
- Verification: all fourteen tests pass, including eight performance tests and 929 paired cases. Actual before/after expressions/effect flows agree in tested cases; UN real scoring/preparation and unaffected definitions preserved. Five-file parsing/unique definitions/BOM/CRLF and diff checks pass; independent Tester PASS and Evaluator ACCEPT for code/source checks.
- Limitations: no game launch, existing-save loading, tooltip-rendering observation or measured speedup. Source/Python checks cannot establish runtime behavior. Upstream generators and shared role/workflow files remain unavailable. Prior city visual acceptance is pending.
- Next action: code/source work complete. A later controlled in-game check should load a copied late-game save and inspect relevant results/tooltips and timings; runtime performance remains unclaimed. Prior city visual checks remain separate.
- Pass history: entries under [history/](history/info.md), linked below as each pass is recorded.
- [Plan the Tech and Res replacement](history/2026-11-10_12-14-01-889548-planner-cleanup-plan.md)
- [Replace old local mods with the Git checkout](history/2026-11-10_12-14-01-947719-orchestrator-replace-mod-checkout.md)
- [Research repository structure and startup override](history/2026-11-10_12-14-01-954207-researcher-repository-structure.md)
- [Research native Russian city pack rules](history/2026-11-10_12-14-01-959504-researcher-native-russian-pack.md)
- [Write repository instructions and current plan](history/2026-11-10_12-14-01-964240-orchestrator-instructions-and-plan.md)
- [Implement Russian city variants](history/2026-11-10_12-15-35-991558-coder-russian-city-variants.md)
- [Tighten skyscraper requirements](history/2026-11-10_12-17-28-499102-coder-skyscraper-review-fixes.md)
- [Independently test city selection and assets](history/2026-11-10_12-20-32-465679-tester-city-selection-and-assets.md)
- [Accept production changes and static evidence](history/2026-11-10_12-20-32-519372-evaluator-production-static-accept.md)
- [Review test behavior after future commits](history/2026-11-10_12-20-32-525285-orchestrator-test-baseline-review.md)
- [Keep preservation tests stable after commits](history/2026-11-10_12-21-27-079520-tester-fixed-import-baseline.md)
- [Reaffirm final code and static acceptance](history/2026-11-10_12-21-27-119401-evaluator-final-static-accept.md)
- [Record completed import and accepted local fixes](history/2026-11-10_12-21-27-125044-orchestrator-final-integration.md)

## Late-game performance investigation

- Requested scope: investigate recurring simulation work and optimization opportunities; no gameplay changes requested.
- Starting state: checkout at `38b06854` with existing uncommitted Russian city fixes, tests and project documentation. Preserve that work.
- Investigation plan: trace actual monthly/yearly callers and nested loops; compare mod and installed game settings; establish supported measurement tools; rank changes by repeated work removed and behavior risk; independently check the report.
- Verification limit: source inspection cannot measure simulation speed. No game or saved campaign has been opened for this investigation.
- Next action: requested investigation complete; deliver findings. Any later optimization must measure baseline and resulting behavior before claiming a gain.

- [Scope the performance investigation](history/2026-11-10_12-26-00-567228-orchestrator-performance-investigation-scope.md)

## Repository documentation and launcher thumbnail

- Goal: expand AGENTS.md across the full mod and add source-backed feature/organization guides.
- Milestone: [Repository documentation](repository-documentation/info.md), complete. This work preserves the separately recorded performance investigation.
- Implemented state: user-confirmed launcher thumbnail at .metadata/thumbnail.png; balanced repo-wide AGENTS.md; fifteen topic guides covering architecture, gameplay, visuals and development, with folder indexes, source-folder guides and explicit feature/evidence status. Docs and AGENTS.md are eligible for versioning. Changes remain local/uncommitted.
- Decisions: completed thumbnail before docs as requested; used actual source and cross-author review. Detailed city instructions moved into a visual guide. Active features, commented/uncalled material, future plans and missing tooling are distinguished. Existing metadata identity, root artwork and gameplay fixes remain unchanged.
- Boundaries: this pass changes documentation and one thumbnail copy only; no new gameplay, launcher DB/playset or installed-game changes from this work. Concurrent performance implementation has begun separately and its files/records are preserved; these documentation reviews do not evaluate its changes.
- Verification: independent Tester passed 71 Markdown files/399 local links before final record appends, UTF-8/replacement-character/whitespace checks and Git scope/ignore checks. Both independent cross-author content reviews returned ACCEPT, covering every guide without self-review; 188 and 256 reviewed links resolved. PNG decode and SHA256 equality passed; user confirmed actual launcher preview. git diff --check passed.
- Limitations: guides document inspected source; they do not establish whole-mod gameplay correctness, balance, save compatibility or performance. Previous city tests cover source selection; city rendering/refresh remains unverified.
- Next action: use docs/info.md and the matching system guide for future work; update guides with behavior changes. No requested documentation work remains. Preserve unfinished performance and Russian city runtime tasks in their own milestones.
- [Research launcher thumbnail convention](history/2026-11-10_12-28-57-545611-researcher-thumbnail-convention.md)
- [Copy artwork to the launcher thumbnail location](history/2026-11-10_12-28-57-573262-coder-thumbnail-copy.md)
- [Accept user-confirmed preview and resume documentation](history/2026-11-10_12-28-57-581721-orchestrator-thumbnail-confirmed-docs-resumed.md)

- [Research game settings and available measurement tools](history/2026-11-10_12-31-23-586961-researcher-engine-settings-research.md)
- [Trace recurring gameplay work](history/2026-11-10_12-31-23-586962-researcher-gameplay-script-research.md)
- [Trace research and political calculations](history/2026-11-10_12-31-23-586963-researcher-research-politics-research.md)
- [Plan a later measured implementation](history/2026-11-10_12-31-23-586964-planner-bounded-optimization-recommendation.md)
- [Independently check critical source claims](history/2026-11-10_12-31-23-586965-tester-independent-source-cross-check.md)
- [Assemble ranked investigation results](history/2026-11-10_12-31-23-586966-orchestrator-performance-report-draft.md)

- Research state: three read-only research reports complete, bounded future plan recorded and final [ranked report](late-game-performance/report.md) independently verified. Tester PASS; Evaluator ACCEPT. Investigation complete.
- Actual verification: six existing city tests passed; git diff --check passed. No gameplay code changed by this investigation; no runtime capture or measured gain.

- [Verify the assembled performance report](history/2026-11-10_12-33-08-135269-tester-final-report-source-pass.md)
- [Accept the source investigation](history/2026-11-10_12-33-08-135270-evaluator-performance-investigation-accepted.md)
- [Integrate the completed investigation](history/2026-11-10_12-33-08-135271-orchestrator-performance-investigation-complete.md)
- [Trace technology, economy, power and development](history/2026-11-10_12-36-23-069178-researcher-economy-research-map.md)
- [Trace politics, population, diplomacy, military and climate](history/2026-11-10_12-36-23-118646-researcher-politics-population-world-map.md)
- [Trace loading, interface, localization and assets](history/2026-11-10_12-36-23-125814-researcher-architecture-ui-assets-map.md)
- [Write research, industry, energy and development guides](history/2026-11-10_12-36-23-131498-coder-economy-guides.md)
- [Write politics, demographics, diplomacy, military and climate guides](history/2026-11-10_12-36-23-136980-coder-politics-world-guides.md)
- [Write architecture, initialization, model and interface guides](history/2026-11-10_12-36-23-142004-coder-architecture-visual-guides.md)
- [Balance instructions and connect whole-mod documentation](history/2026-11-10_12-36-23-147143-orchestrator-balanced-repo-instructions.md)

## Gameplay-preserving performance implementation

- Goal: remove proven repeated work without changing existing campaign rules, stored data, random choices or update dates.
- Active milestone: [gameplay-preserving performance](behavior-preserving-performance/info.md), implementation in progress. Prior audit is complete; preserve separate documentation and city milestones.
- Implemented state: accepted five-change plan and exclusive ownership; source-based differential tests being written independently.
- Decisions/boundaries: keep population identities, AI cadence, UN retry budget and proposer lookup behavior; no saves, playsets, personal settings or installed game edits.
- Verification: source research complete; fresh implementation tests and independent evaluation pending.
- Limitations: no game session or timing capture; Python evaluation cannot prove runtime behavior.
- Next action: finish implementation, test baseline/current values and cleanup, then independently evaluate.
- [Start gameplay-preserving performance work](history/2026-11-10_12-38-17-956663-orchestrator-authorize-preserving-performance.md)
- [Accept the bounded implementation plan](history/2026-11-10_12-38-17-956664-planner-preserving-performance-plan.md)
- [Check documentation links, encoding and file scope](history/2026-11-10_12-38-50-239487-tester-documentation-links-scope.md)
- [Accept cross-author political and world-system guides](history/2026-11-10_12-38-50-287421-evaluator-political-world-docs-accept.md)
- [Accept cross-author architecture, visuals and economy guides](history/2026-11-10_12-38-50-295011-evaluator-architecture-economy-docs-accept.md)
- [Complete balanced whole-mod documentation](history/2026-11-10_12-38-50-301253-orchestrator-documentation-final-integration.md)
- [Preserve concurrent performance implementation](history/2026-11-10_12-39-48-561140-orchestrator-preserve-concurrent-performance.md)

- [Confirm temporary value restoration](history/2026-11-10_12-40-59-953712-researcher-pollution-temporary-syntax.md)
- [Reuse UN country inputs within law comparisons](history/2026-11-10_12-40-59-953713-coder-un-paired-context-reuse.md)
- [Implement the remaining four local cleanups](history/2026-11-10_12-40-59-953714-orchestrator-implement-local-performance-cleanups.md)

- Performance implementation state: all five local cleanups implemented. [Changes](behavior-preserving-performance/changes.md) and affected-folder guides added. Initial structural/encoding checks, six city tests and diff check pass; independent before/after tests and Evaluator review in progress.

- [Document calculation reuse and initial checks](history/2026-11-10_12-42-42-988241-orchestrator-performance-guides-and-initial-checks.md)

- [Pass original/current calculation checks](history/2026-11-10_12-45-22-213849-tester-performance-differential-tests-pass.md)
- [Accept gameplay-preserving performance code](history/2026-11-10_12-45-22-213850-evaluator-preserving-performance-code-accepted.md)
- [Integrate accepted calculation cleanups](history/2026-11-10_12-45-22-213851-orchestrator-preserving-performance-integration.md)

- Final performance implementation state: five cleanups implemented; fourteen tests pass; independent Tester PASS and Evaluator ACCEPT for code/source checks. [Changes and actual evidence](behavior-preserving-performance/changes.md). No runtime save-loading or speed claim.

## Publication of reviewed updates

- Goal: publish the tested local mod after the user requested push.
- Active milestone: [publish reviewed updates](publish-reviewed-updates/info.md), implementation published and remote verified at `2ceab5fd`.
- Scope: performance cleanups/tests plus earlier reviewed city, thumbnail and repository documentation.
- Verification: fetched origin/main matches local base; fourteen tests and diff checks pass.
- Next action: publish the documentation-only outcome record and verify final remote/tree status; runtime observations remain separate.
- [Prepare reviewed mod updates for publication](history/2026-11-10_12-50-23-389429-orchestrator-publication-preflight.md)

- [Publish and verify reviewed mod updates](history/2026-11-10_12-51-10-791895-orchestrator-reviewed-updates-published.md)
- Publication result: `2ceab5fd91b85ce3fe4ec15e73a3d7ebc5cff1ae` pushed to origin/main; remote SHA matched and tree was clean before this documentation record.
