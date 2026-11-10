# Paradox launcher thumbnail

- Goal: show the mod's existing artwork in the Paradox launcher preview.
- Scope: copy root `thumbnail.png` to `.metadata/thumbnail.png`; preserve artwork and mod identity.
- Completion criteria: valid image, byte-identical copy, and observed working launcher preview.
- Status: complete. The user confirmed “it works” on 2026-11-10. The copy is a valid 512 by 512 RGB PNG; both images share SHA256 `7DA85C949E12AC7AB8F0C82DAFC260F8D92783CD8A2A4EF6A17837ABA4B1ADD1`.
- Boundaries: no launcher database, playset, identity or original-image edit. Root artwork is retained; the separate DLC-style preview has its own thumbnail under `dlc/dlc_ztr/`.
