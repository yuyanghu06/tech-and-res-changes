# Tech & Res documentation

This is a map of the current mod for future contributors and LLM sessions. It describes active source inspected on 2026-11-10, including the local Russian city fixes and launcher thumbnail. It is not a claim that every feature has been played or tested. Start with [feature status](development/feature-status.md) and the guide for your task; follow the linked definitions before changing behavior.

## Find the relevant system

| Question or change | Read |
| --- | --- |
| How does the engine read this repository? | [Repository map](architecture/repository-map.md) |
| What runs at game start, each month or each year? | [Startup and periodic work](architecture/startup-and-periodic-work.md) |
| Technology tree, Research Center and research agreements | [Technology and research](gameplay/technology-and-research.md) |
| Goods, factories, data, software and AI services | [Economy and digital industry](gameplay/economy-and-digital-industry.md) |
| Resources, power plants and national electricity | [Energy and resources](gameplay/energy-and-resources.md) |
| Companies, branded goods and national development | [Companies and development](gameplay/companies-and-development.md) |
| Laws, parties, political direction and interest groups | [Politics and laws](gameplay/politics-and-laws.md) |
| Demographic transition, population and new-country initialization | [Demographics](gameplay/demographics.md) |
| UN votes, institutions, unification and country-specific paths | [Diplomacy and country content](gameplay/diplomacy-and-country-content.md) |
| Army, navy, nuclear programs, deterrence and strikes | [Military and nuclear systems](gameplay/military-and-nuclear.md) |
| Warming, policy effects and climate disasters | [Climate and environment](gameplay/climate-and-environment.md) |
| City styles, model selection and military assets | [Cities and military models](visuals/cities-and-military-models.md) |
| Journal controls, icons, localization and launcher preview | [Interface, localization and metadata](visuals/interface-localization-and-metadata.md) |
| How to make and check a change | [Editing and verification](development/editing-and-verification.md) |

## Reading rules

Read the entry point, conditions, calculated values, effects and callers as one system. An identifier in a commented block, a filename, an icon or translated text does not by itself establish an active feature. Names can be misleading: `pm_computerized_research_center` is attached to universities; the old research-agreement shortcut is disabled while its treaty article is active.

Active script values take precedence over stale explanatory comments. Era comments extend into 2051, but the active end date is `2036.1.1`. The upstream changelog also contains older game-version notes. Treat [the current source map](architecture/repository-map.md) and exact definitions as the starting point.

These pages explain major systems and their connections, not every balance value or individual company/event. Search the exact identifier when working below that level. When a source change makes a guide inaccurate, update that guide and [feature status](development/feature-status.md) in the same pass.

## Records and folders

- [Architecture](architecture/info.md), [gameplay](gameplay/info.md), [visuals](visuals/info.md) and [development](development/info.md) organize the guides.
- [AGENTS.md](../AGENTS.md) contains repo-wide working instructions.
- [Project notes](../notes.md) preserve dated user requests and observations.
- [Milestone snapshot](../milestones/milestone.md) and [work list](../milestones/to-do.md) record current tasks. Preserve separate investigations rather than replacing their records.
- [The history template](templates/history-entry.md) defines append-only pass records; it is not a gameplay document.
