# Research launcher thumbnail convention

- Local timestamp / acting role / milestone: 2026-11-10 12:28:57.545611 -05:00 America/New_York / researcher / launcher-thumbnail
- Requested scope: Find the expected preview image location.
- Starting repository state: Root thumbnail valid; metadata image absent.
- Work performed / changed files: Read-only comparison of twelve installed Workshop mods and launcher MetadataFormatService.
- Decisions: Use .metadata/thumbnail.png without changing metadata identity or adding a guessed JSON field.
- Checks and evidence: Working mods and launcher thumbnail.png constant support expected location. Root image is also referenced separately by mod DLC.
- Resulting state / acceptance: One-file copy plan accepted.
- Remaining work and handoff: Copy unchanged artwork and verify preview.
