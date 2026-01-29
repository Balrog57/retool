# Retool Unified

> [!IMPORTANT]
> **Retool Unified** est un travail de préservation et d'évolution du projet original Retool.
> J'ai fusionné les 3 dépôts originaux (programme, données, documentation) qui étaient à l'abandon pour en faire une **version unique, stable et 100% autonome**.

Retool is a filter utility for [Redump](http://www.redump.org/) and [No-Intro](https://datomatic.no-intro.org/index.php?page=download)
DAT files. By customizing the DAT files before you load them into a ROM manager, you can more
effectively trim, consolidate, and deduplicate your ROM sets.

![A screenshot of the main Retool screen](images/main-app.png)

Retool Unified offers the following features:

* **Fully Autonomous**: No external downloads required at startup. All configuration files, clone lists, and metadata are bundled with the application.

* Superior One Game, One ROM (1G1R) functionality compared to other tools.

* Priority-based region and language filtering.

* Exclusions of unwanted titles like demos, applications, and more.

* Custom regular expression filters for including or excluding titles.

* Local filenames for titles, such as <code>シャイニング·フォースⅡ 『古の封印』</code>
  instead of <code>Shining Force II - Inishie no Fuuin</code>.

* CLI and GUI versions.

You add your DAT files to Retool, and it creates new DAT files with all your preferences,
leaving the originals intact. You can then load the new DAT files in a ROM manager like
[RomVault](https://www.romvault.com/), [CLRMamePro](https://mamedev.emulab.it/clrmamepro/),
or [IGIR](https://www.igir.io) to do your file management &mdash; you just don't need to
use their 1G1R modes, as Retool has already done the work for you.

Retool is supported on Windows 10+, Ubuntu 20+, and macOS 15+. Non-compiled versions
require Python 3.10 or higher.

## Documentation and Data

This repository now includes all necessary data:
- `clonelists/`: Clone lists for 1G1R processing.
- `metadata/`: Metadata files for improved filtering.
- `config/`: Configuration files.
- Documentation sources are also integrated.

