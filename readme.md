# Retool Unified

> [!IMPORTANT]
> **Retool Unified** est un travail de préservation et d'évolution du projet original Retool.
> J'ai fusionné les 3 dépôts originaux (programme, données, documentation) qui étaient à l'abandon pour en faire une **version unique, stable et 100% autonome**.

Retool est un utilitaire de filtrage pour les fichiers DAT [Redump](http://www.redump.org/) et [No-Intro](https://datomatic.no-intro.org/index.php?page=download). En personnalisant les fichiers DAT avant de les charger dans un gestionnaire de ROMs, vous pouvez trier, consolider et dédupliquer vos ensembles de ROMs de manière plus efficace.

![Une capture d'écran de l'écran principal de Retool](images/main-app.png)

Retool Unified offre les fonctionnalités suivantes :

* **Entièrement Autonome** : Aucun téléchargement externe requis au démarrage. Tous les fichiers de configuration, listes de clones et métadonnées sont inclus avec l'application.

* Fonctionnalité One Game, One ROM (1G1R) supérieure à celle des autres outils.

* Filtrage basé sur la priorité des régions et des langues.

* Exclusion des titres indésirables comme les démos, les applications, et plus encore.

* Filtres d'expressions régulières personnalisés pour inclure ou exclure des titres.

* Noms de fichiers locaux pour les titres, tels que <code>シャイニング·フォースⅡ 『古の封印』</code>
  au lieu de <code>Shining Force II - Inishie no Fuuin</code>.

* Versions CLI (ligne de commande) et GUI (interface graphique).

Vous ajoutez vos fichiers DAT à Retool, et il crée de nouveaux fichiers DAT avec toutes vos préférences, en laissant les originaux intacts. Vous pouvez ensuite charger les nouveaux fichiers DAT dans un gestionnaire de ROMs comme [RomVault](https://www.romvault.com/), [CLRMamePro](https://mamedev.emulab.it/clrmamepro/), ou [IGIR](https://www.igir.io) pour gérer vos fichiers &mdash; vous n'avez tout simplement pas besoin d'utiliser leurs modes 1G1R, car Retool a déjà fait le travail pour vous.

Retool est supporté sur Windows 10+, Ubuntu 20+, et macOS 15+. Les versions non compilées nécessitent Python 3.10 ou supérieur.

## Documentation et Données

Ce dépôt inclut désormais toutes les données nécessaires :
- `clonelists/` : Listes de clones pour le traitement 1G1R.
- `metadata/` : Fichiers de métadonnées pour un filtrage amélioré.
- `config/` : Fichiers de configuration.
- Les sources de la documentation sont également intégrées.
