# City appearance

`city_types/` chooses building model pools from state-region, technology and DLC conditions. `city_centerpiece/` associates central models with those named city types. Higher city-type weights win. Shared geographic and technology checks live in `common/scripted_triggers/ztr_city_graphics_triggers.txt`.

Many existing files are generated outputs whose generators are absent. Keep focused changes separate where possible and verify both the selected type and its centerpiece.

[The full visual guide](../../../docs/visuals/cities-and-military-models.md) explains geographic/technology selection, Russian DLC guards, shared assets and the current verification limits.
