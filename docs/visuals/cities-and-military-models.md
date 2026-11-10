# City and military models

Gameplay definitions decide what exists; map definitions decide which model represents it. Editing a unit's statistics or a building's technology requirement does not automatically change every image or map model. Follow the named references across these layers.

## Cities and rural hubs

[ztr_city_graphics_triggers.txt](../../common/scripted_triggers/ztr_city_graphics_triggers.txt) defines geographic zones, government conditions, and six technology stages:

| City stage | Required technology |
| --- | --- |
| Early modern start | `elevator` |
| Early modern | `paved_roads` |
| Late modern | `highway_systems` |
| Postmodern | `multinational_corporations` |
| Digital | `circular_economy` |
| AI | `agentic_ai` |

The stage names and date comments describe intended styles; the actual checks use technology. Zone conditions cover regions such as North America, Eastern Europe, China, and Japan/Korea. Conditions run against a state region, which can contain states owned by different countries. Technology checks inspect owners through `any_scope_state`.

[city_types/](../../gfx/map/city_data/city_types/) contains residential pools, other building mappings, and selection weights. Higher matching weights take priority. Repeated mesh entries affect the supplied pool proportions; preserve duplicates intentionally. Socialist variants add government checks and weights. Rural hubs have separate files. [city_centerpiece/](../../gfx/map/city_data/city_centerpiece/) connects selected type names to central-city entities through `city_graphics_type`.

## Russian pack change

[ztr_eeu_russian_city.txt](../../gfx/map/city_data/city_types/ztr_eeu_russian_city.txt) adds ten city-only variants of the generic Eastern European definitions. Each retains its original technology and socialist checks, adds `ip5_cosmetics` plus `russian_buildings_trigger`, and raises the corresponding base weight by three. Historical residential, civic, and factory models use the native Russian pack; custom modern model occurrences remain intact. The existing types provide a fallback when the pack or geographic check does not match.

[ztr_eeu_russian_cities.txt](../../gfx/map/city_data/city_centerpiece/ztr_eeu_russian_cities.txt) supplies matching centerpieces. Historical stages use native Russian entities; later stages retain custom models. Each skyscraper centerpiece explicitly requires an existing skyscraper that is under construction or has a completed level. The historical skyscraper uses two separate attachments, matching the native pack.

Eight state-only Eastern European test overrides were removed because they bypassed technology. The three unrelated African test definitions remain in both `ztr_city_test.txt` files. Do not treat those remaining tests as normal technology-controlled examples. Original generated production files and rural definitions were preserved. Their referenced generator scripts and design document are absent; the new Russian files are hand-maintained.

## Military visuals

[combat_unit_types/](../../common/combat_unit_types/) defines unit gameplay, upgrades, requirements, and illustrations. [ship_types/](../../common/ship_types/), [ship_modifications/](../../common/ship_modifications/), and [ship_modification_slots/](../../common/ship_modification_slots/) define naval gameplay and equipment.

[front_entities/](../../gfx/map/front_entities/) chooses battlefield entities using unit and culture conditions. [ztr_navy_fleet_entities.txt](../../gfx/map/fleet_entities/ztr_navy_fleet_entities.txt) connects ships and equipment slots to fleet models. For example, it references modern carrier entities defined under [navy_modular/aircraftcarrier_modern/](../../gfx/models/military/navy_modular/aircraftcarrier_modern/). Unit pictures live separately in [unit_illustrations/](../../gfx/unit_illustrations/).

Asset declarations connect named entities and meshes to geometry and textures. Preserve those names together; a folder named `unused` or `navies_backup` is not proof its contents are unloaded. The [focused tests](../../tests/info.md) check city conditions and references, not rendering or military balance. Russian model names were checked against installed assets, but city appearance and live technology transitions remain unobserved. Use [the editing guide](../development/editing-and-verification.md) and report those limits plainly.
