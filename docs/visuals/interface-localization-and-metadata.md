# Interface, localization, and metadata

Most Tech & Res controls use Victoria 3's journal system. The repository does not define a separate application interface. A displayed control can depend on a journal entry, button, calculated value, conditional text, and picture in different folders.

## Find the visible control

[gui/ztr_texticons.gui](../../gui/ztr_texticons.gui) and [gui/01_goods_texticons.gui](../../gui/01_goods_texticons.gui) define inline text icons. They are the only two `.gui` files there; the folder also has a documentation guide. Do not describe it as the owner of all custom panels.

Actual panel definitions include:

- `je_research_center` in [ztr_je_technology.txt](../../common/journal_entries/ztr_je_technology.txt): research philosophy, nuclear and energy projects, and an innovation map.
- `je_un_info_panel` and `je_un_votations` in [ztr_je_un.txt](../../common/journal_entries/ztr_je_un.txt): UN information and voting controls.
- `je_demography`, `je_development`, `je_global_warming`, and `je_liberty_index` in their respective [journal-entry files](../../common/journal_entries/).

[scripted_buttons/](../../common/scripted_buttons/) owns availability and effects; [scripted_progress_bars/](../../common/scripted_progress_bars/) supplies progress displays. [ztr_journal_entry_sguis.txt](../../common/scripted_guis/ztr_journal_entry_sguis.txt) builds lists and tooltips for colonial states, electricity-grid gaps, political powers, polluters, and climate disasters. [customizable_localization/](../../common/customizable_localization/) selects conditional descriptions. Journal groups provide illustrations, while journal `map_color` and `map_tooltip` blocks use calculated values and named colors. These are source-defined features, not an assertion that every panel has been tested in game.

## Text and media

The 2026-11-10 source snapshot has **308 localization files across eleven language folders**, twenty-eight files per language. All have a UTF-8 byte-order mark and a matching `l_english:`, `l_russian:`, or other language header. Preserve the BOM, key names, and expressions inside strings. Matching file counts do not prove complete or accurate translations.

[localization/english/replace/overwriting_l_english.yml](../../localization/english/replace/overwriting_l_english.yml) renames existing game content. Other keys are a mix of inherited names and mod-specific identifiers; a `ztr_` filename does not mean every key has that prefix. Translation fallback behavior has not been checked by this research. Do not promote a changelog claim about fallback into verified engine behavior.

[gfx/interface/](../../gfx/interface/) supplies icons and journal illustrations. [ztr_media_aliases.txt](../../gfx/media_aliases/ztr_media_aliases.txt) associates media names with videos, sound events, and fallback aliases; videos and pictures live under [gfx/event_pictures/](../../gfx/event_pictures/). Check the caller and fallback when changing a media reference.

## Launcher metadata and DLC presentation

[.metadata/metadata.json](../../.metadata/metadata.json) identifies local mod `tech.res`, displayed as `[1.15] Tech & Res`, supporting `1.15.*`; its dependency list is empty. [.metadata/thumbnail.png](../../.metadata/thumbnail.png) is an exact copy of [the retained root image](../../thumbnail.png). Its launcher display was confirmed by the user.

The separate [dlc_ztr.dlc](../../dlc/dlc_ztr/dlc_ztr.dlc) and [dlc_ztr.dlc.json](../../dlc/dlc_ztr/dlc_ztr.dlc.json) describe the mod's DLC-style presentation. The JSON's `thumbnailPath = "thumbnail.png"` resolves to the image **inside `dlc/dlc_ztr/`**, not the root image. [tech_res_dlc_metadata.txt](../../dlc_metadata/tech_res_dlc_metadata.txt) registers `dlc_tech_res`. These identifiers are distinct from paid game-pack checks such as `ip5_cosmetics`.

Preserve identity fields unless an identity change is requested. A thumbnail fix does not require changing launcher databases, playsets, or caches. Follow [editing and verification](../development/editing-and-verification.md), and keep launcher confirmation separate from untested in-game panels and rendering.
