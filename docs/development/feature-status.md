# Current features and verification status

Source snapshot: 2026-11-10, imported commit `38b0685472188a42ca7dee4adb047b6a0b4c61f6` plus the local Russian city and thumbnail changes. This is a source-backed feature map, not a claim that every system has been played successfully. Check active definitions before relying on a changelog, translated name or old TODO.

## Active source areas

| System | Current source describes | Guide |
| --- | --- | --- |
| Extended technology/research | Eleven eras, new technologies and patches, Research Center programs, research philosophy and treaty agreements | [Technology and research](../gameplay/technology-and-research.md) |
| Industry and consumption | New goods/industries, digital data/software/AI connections, production methods and population demand | [Economy](../gameplay/economy-and-digital-industry.md) |
| Power/resources | Additional deposits/extraction, geography-dependent generation, national-electricity conversion and grid stations | [Energy](../gameplay/energy-and-resources.md) |
| Companies/development | Sector companies, branded/generic prestige goods, country development tiers and related modifiers | [Companies and development](../gameplay/companies-and-development.md) |
| Politics/laws | Liberty/Equality indexes, political direction, modern ideologies/movements and additional law groups | [Politics](../gameplay/politics-and-laws.md) |
| Population | Demographic progress/stages, economic/social inputs, periodic histories and new-country handling | [Demographics](../gameplay/demographics.md) |
| Diplomacy/country content | UN governance/institutions, voting, decolonization, unification and specified country paths | [Diplomacy](../gameplay/diplomacy-and-country-content.md) |
| Military/nuclear | Modern units, ship types/equipment, nuclear programs, operational arsenals and related diplomacy | [Military](../gameplay/military-and-nuclear.md) |
| Climate | Temperature/stages, policy effects and rule-controlled climate disasters | [Climate](../gameplay/climate-and-environment.md) |
| Presentation | Technology-selected city styles, modern military models, journal controls, icons, text and mod previews | [Models](../visuals/cities-and-military-models.md); [interface](../visuals/interface-localization-and-metadata.md) |

Counts in the guides are counts of inspected source definitions/patch blocks, not the engine's combined totals after base-game and DLC loading. Era comments reach 2051, but [the active end-date setting](../../common/defines/ztr_defines.txt) is `2036.1.1`.

## Inactive, misleading or unfinished material

- The old quick research-agreement [diplomatic action](../../common/diplomatic_actions/ztr_propose_research_agreement.txt) is commented out. The [treaty article](../../common/treaty_articles/ztr_research_agreement.txt) is active.
- `nuclear_reactor` is not normally researchable in the technology tree; Research Center or purchase routes supply it. Separately named nuclear-power-plant and spaceport building blocks inspected by researchers are commented out. This does not mean nuclear generation or space-industry methods are absent.
- `pm_computerized_research_center` belongs to university production, despite its name.
- Future continental superstate country/flag/name data do not establish a reachable formation system. Do not describe the removed EU mechanics or a TODO as restored gameplay.
- Permanent terrain flooding, arable-land loss and building removal in climate comments are not implemented by those TODOs. Active coastal-disaster effects are different; see the climate guide.
- The legacy fallout event labeled disabled has a definition but no normal caller found in the source search. Carrier air-wing customization blocks inspected by researchers are commented out.
- Folder names such as `unused` and `navies_backup` do not alone establish that their contents are unloaded. Inspect the definitions/references before deleting or declaring them inactive.
- The remaining African city tests are existing state-only test entries, outside the earlier Russian fix. Do not claim all temporary tests were removed.

## Evidence actually obtained

- **Launcher thumbnail:** the existing artwork was copied to `.metadata/thumbnail.png`; PNG decode and identical hashes were checked. The user confirmed the launcher preview works.
- **Russian city change:** six independent source tests passed, including technology/DLC/geography selection and skyscraper construction/level checks. All 91 referenced Russian/custom meshes/entities resolved in local assets. Independent code/static review accepted the change.
- **Not established:** in-game city appearance or refresh after research; gameplay, balance, save compatibility or engine performance of the other systems. Reading their scripts establishes defined behavior, not a successful runtime test.
- **Localization:** all 308 inspected `.yml` files had UTF-8 BOMs across eleven language folders. Translation accuracy was not checked.

There is no supplied whole-mod build/test pipeline. The city generator scripts, their cited design document and historical technology audit documents are absent from this checkout. Do not invent them or imply that the new guides recreate them. Performance investigation and implementation are recorded separately in [project milestones](../../milestones/milestone.md); concurrent edits to shared helpers are outside this documentation review. Read those records before changing the same files, and preserve their measurement limits.

## Gameplay-preserving performance work, 2026-11-10

Five local calculation cleanups are implemented: environmental support reuse, UN preparation reuse, paused nuclear gain checks, research cap display and early exclusion of ineligible nuclear attackers. [The implementation record](../../milestones/behavior-preserving-performance/info.md) tracks independent before/after source tests and review. All fourteen tests pass, including eight performance tests with 929 paired fixtures; source structure/encoding and diff checks pass. Independent Evaluator ACCEPT applies to code/source checks. Existing-save loading, game tooltips and simulation speed have not been observed.
