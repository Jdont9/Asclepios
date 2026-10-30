> [!WARNING]
> ### Ceci est un fork de l'application [originale](https://github.com/Divested-Mobile/Hypatia) (abandonnée) de DivestOS.
> ### Ce dépôt ([Jdont9/Hypatia](https://github.com/Jdont9/Hypatia)) est **Asclépios AV**, mon fork personnel de [MaintainTeam/Hypatia](https://github.com/MaintainTeam/Hypatia), voir [Modifications de ce fork](#modifications-de-ce-fork-450).

![Bannière](./fastlane/metadata/android/en-US/images/featureGraphic.png)

Asclépios AV
============
_Un fork d'[Hypatia](https://github.com/MaintainTeam/Hypatia), créé à l'origine par Divested Computing Group._

Vue d'ensemble
--------------
Asclépios AV est un fork d'Hypatia, le premier scanner de logiciels malveillants FOSS (logiciel libre) au monde pour Android. Il est propulsé par des bases de données de signatures de style ClamAV.

[<img src="https://gitlab.com/IzzyOnDroid/repo/-/raw/master/assets/IzzyOnDroid.png"
     alt="Hypatia d'origine sur IzzyOnDroid"
     height="80">](https://apt.izzysoft.de/packages/org.maintainteam.hypatia/)
[<img src="https://hosted.weblate.org/widget/maintainteam/hypatia/287x66-grey.png"
     alt="État des traductions (Hypatia d'origine)"
     height="66">](https://hosted.weblate.org/projects/maintainteam/hypatia/)

<a id="modifications-de-ce-fork-450"></a>
Modifications de ce fork (4.5.0)
------------------------------
Asclépios AV (identifiant d'application `fr.jd.asclepios`) est [mon fork personnel](https://github.com/Jdont9/Hypatia) de [MaintainTeam/Hypatia](https://github.com/MaintainTeam/Hypatia), lui-même un fork de l'application abandonnée [Divested-Mobile/Hypatia](https://github.com/Divested-Mobile/Hypatia). Les APK signés sont sur la [page des Releases](https://github.com/Jdont9/Hypatia/releases). Par rapport à la branche `stable` d'origine (3.18) :

- **Recherche d'URL malveillantes dans les fichiers (4.5.0, optionnel) :** cherche les adresses web contenues dans les APK (code DEX et assets texte) et les fichiers de type texte, et compare leur hôte à la base de domaines malveillants. Une correspondance rejoint les menaces actives. Nécessite l'analyseur de liens (il télécharge la base de domaines). Le manifeste et les ressources binaires d'un APK ne sont pas lus.
- **Liste de fichiers de confiance (4.5.0) :** « Toujours ignorer » sur une menace ajoute le SHA-256 du fichier à une liste blanche : il n'est plus jamais signalé. La liste peut être importée depuis un fichier texte (un SHA-256 par ligne), consultée et vidée dans Paramètres → Avancé. Une liste blanche en ligne de fichiers sains (`hypatia-whitelist-sha256-bloom.bin`, même format bloom signé que les autres bases) est téléchargée et chargée avec les bases de signatures ; elle se désactive dans Paramètres → Mises à jour.
- **Import NSRL (4.5.0, optionnel, manuel) :** Paramètres → Avancé → Liste NSRL importe les SHA-256 d'APK Android connus préparés à partir du NSRL du NIST, pour qu'ils ne soient jamais signalés. Voir [le tutoriel](#importer-la-liste-blanche-nsrl-optionnel).
- **Menaces actives (4.5.0) :** une nouvelle ligne « Menaces actives » sur l'écran d'accueil ouvre la liste des menaces encore actives. Chaque menace indique pourquoi elle a été signalée (correspondance dans la base de signatures et type d'empreinte, fichier, SHA-256, date), avec recherche VirusTotal, suppression / désinstallation et ignorer. Une menace reste listée jusqu'à la suppression du fichier, la désinstallation de l'application ou son abandon par l'utilisateur.
- **Fichiers leurres anti-rançongiciel (4.5.0, optionnel) :** fichiers appâts dans Download, Documents, Pictures et DCIM. Si une application en modifie, renomme ou supprime un, vous recevez une alerte et l'appât est remis en place. Fonctionne uniquement quand le scanner temps réel tourne ; un rançongiciel qui ne cible que certaines extensions peut ignorer un appât `.txt`.
- **Détection de renommage en masse (4.5.0, optionnel) :** alerte quand au moins 15 fichiers reçoivent un suffixe en 10 secondes, signature d'un rançongiciel qui chiffre les fichiers sur place. Nécessite le scanner temps réel.
- **Refonte graphique (4.4.0) :** thème rouge (clair et sombre), carte d'état avec tuiles signatures et dernière mise à jour, gros bouton Lancer / Arrêter l'analyse et badge indiquant si la protection en temps réel est active. Le journal reste masqué tant qu'on n'appuie pas sur « Afficher le journal ».
- **Page de paramètres (4.4.0) :** un écran de paramètres par catégories (Réseau, Mises à jour, Protection, Analyses, Avancé), ouvert par l'icône d'engrenage, remplace le menu à trois points. Les options d'analyse (applications, stockage externe, stockage amovible, analyse approfondie, /system) sont désormais conservées d'un lancement à l'autre.
- **Dernière analyse (4.4.0) :** une nouvelle carte de l'écran principal affiche la date de la dernière analyse terminée, son résultat (menaces détectées ou aucune) et le nombre de fichiers vérifiés.
- **Options de mise à jour automatique (4.4.0) :** choix de la fréquence (toutes les 6 h, 12 h, une fois par jour, tous les 2 jours, une fois par semaine) et du réseau autorisé (Wi-Fi uniquement, Wi-Fi + données mobiles hors itinérance, ou tous réseaux itinérance comprise). Le réglage par défaut reste une fois par jour en Wi-Fi. Activer les mises à jour automatiques planifie désormais une première vérification immédiate.
- **Animation d'analyse (4.4.1) :** le bouclier d'Asclépios tourne pendant une analyse (animation par images légère, environ 90 Ko).
- **Écran d'accueil (4.4.1) :** le numéro de version s'affiche sous le nom, la tuile de dernière mise à jour indique aussi l'heure, la carte principale occupe plus de hauteur d'écran et le journal utilise la même police que le reste de l'application.
- **Date des bases (4.3.1) :** l'écran principal affiche la date et l'heure de la dernière mise à jour des bases sous le nombre de signatures.
- **Vérification manuelle des mises à jour (4.3.1) :** une nouvelle entrée « Rechercher une mise à jour de l'application » (Paramètres → Avancé) interroge la dernière release de ce dépôt sur GitHub uniquement quand on la touche (jamais automatiquement) et propose d'ouvrir la page de la release.
- **Serveurs de bases (4.3.1) :** le serveur par défaut est désormais [Jdont9/HypatiaDatabases](https://github.com/Jdont9/HypatiaDatabases) (clé de signature `B93D98077D1C`), les serveurs Maintain Team (Codeberg et miroir GitHub) restent disponibles, et le README liste chaque serveur avec sa clé de signature.
- **Nom et identité :** l'application s'appelle désormais **Asclépios AV** avec l'identifiant `fr.jd.asclepios` : elle s'installe à côté d'Hypatia et ne partage pas ses réglages. Elle a une nouvelle icône, tous les libellés « Hypatia » affichés dans l'application ont été renommés, la licence affichée dans l'application est corrigée en AGPL-3.0 (comme dans `LICENSE`) et une ligne de copyleft pour ce fork a été ajoutée. Les attributions et crédits d'origine sont conservés.

- **Modernisation :** suppression d'`AsyncTask` (déprécié) : les analyses et les téléchargements de bases tournent sur un pool de threads dédié, et les journaux et notifications partent toujours du thread principal ; une exception pendant une analyse est désormais journalisée au lieu de faire planter l'application.
- **Cible Android 16 :** `targetSdk` passé de 34 à 36, avec gestion de l'affichage bord à bord, suppression de la surcharge de `onBackPressed()` (geste retour prédictif) et déclaration de `PROPERTY_SPECIAL_USE_FGS_SUBTYPE` sur les deux services de premier plan.
- **Rotation / grands écrans :** le verrouillage en portrait est retiré et les changements de configuration (rotation, redimensionnement, pliage) ne recréent plus l'activité principale, ce qui conserve le journal.
- **Traductions :** traduction française complète (avertissement, noms des serveurs de bases, analyseur de liens et notifications manquaient), textes des notifications (`Domaine :` / `Fichier :`) et libellés des services déplacés dans des ressources traduisibles, et intégration des mises à jour Weblate de la PR amont #98 (bg, de, et, fi, pl, ro, ru).
- **Analyseur de liens :** la base de domaines est désormais chargée automatiquement (après vérification de sa signature GPG) quand l'analyseur en a besoin, sans dépendre du scanner temps réel ni d'une analyse manuelle (d'après la PR amont #94).
- **Bases disponibles après un démarrage à froid :** l'application restaure sa liste de bases au lancement, donc l'analyse manuelle et l'analyseur de liens n'affichent plus « aucune base » alors que les fichiers sont déjà sur l'appareil (d'après un correctif de la PR amont #101).
- **Analyse root :** une nouvelle option « Analyse approfondie (root) » (Paramètres → Analyses) calcule les empreintes de /system, /vendor, /product, /data (y compris les données privées des autres applications) et des autres partitions système via un shell root (`su`), avec les commandes `md5sum`, `sha1sum` et `sha256sum` de l'appareil. Depuis Android 11, une application ne voit que ses propres données dans `/data/data` : le shell est donc lancé avec `su --mount-master` (espace de montage global, comme le fait SD Maid), avec un retour à `su` simple et un avertissement. Rien n'est installé et aucune dépendance n'est ajoutée. Les cases système / applications / stockage interne continuent de fonctionner seules (sans root, ou si le root est refusé) ; quand l'analyse root réussit, elles sont ignorées car déjà couvertes. Les détections s'affichent avec les notifications habituelles, mais supprimer un fichier situé dans un emplacement protégé depuis la notification est impossible sans root.
- **Applications installées ou mises à jour :** tant que le scanner en temps réel tourne, les APK des applications en cours d'installation ou de mise à jour sont analysés automatiquement.
- **Vérifications de cohérence des bases :** les téléchargements vides ou tronqués sont rejetés (le fichier précédent est conservé), les bases vides sont refusées au chargement, et un avertissement s'affiche si les signatures de test intégrées sont absentes.
- **Workflow de publication :** pousser un tag `v*` (par exemple `v4.5.0`) compile, signe et publie désormais automatiquement une release GitHub depuis ce dépôt, au lieu de celui de MaintainTeam.
- **Documentation :** le README français a été réécrit pour correspondre à la version anglaise.

Non repris de l'amont : la refonte de l'interface de la PR #101 (carte de progression et liste des menaces), que les mainteneurs ont demandé de proposer séparément.

Importer la liste blanche NSRL (optionnel)
------------------------------------------

Le [NSRL](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl) (National Software Reference Library du NIST) recense les empreintes d'un très grand nombre de fichiers logiciels connus, dont des applications Android. Importer les empreintes des **fichiers APK** connus évite qu'ils soient signalés. C'est entièrement optionnel et manuel, car la base est bien trop grosse pour être fournie ou lue sur un téléphone : on prépare un petit fichier texte sur un ordinateur, puis on l'importe.

« Connu » dans le NSRL veut dire répertorié, pas sûr à coup sûr, et un fichier de confiance l'emporte sur une signature. N'importez la liste que si vous l'acceptez.

1. **Téléchargez** le jeu *android* (ou *android minimal*, plus petit) depuis la page [Current RDS Hash Sets](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds) et décompressez-le sur un ordinateur. C'est une base SQLite qui peut atteindre **plusieurs dizaines de gigaoctets** décompressée. Lisez le `README` du jeu et la [documentation RDSv3](https://s3.amazonaws.com/rds.nsrl.nist.gov/RDS/RDSv3_Docs/RDSv3.pdf).
2. **Installez** l'outil en ligne de commande [`sqlite3`](https://www.sqlite.org/download.html) et vérifiez la table : `sqlite3 -readonly RDS_android.db ".schema FILE"` doit montrer les colonnes `sha256` et `file_name`.
3. **Exportez** les SHA-256 des seuls fichiers APK (l'appli hashe des fichiers entiers, seules les entrées qui sont des APK servent). Cela peut être long sur une grosse base :

   ```
   sqlite3 -readonly RDS_android.db "SELECT DISTINCT lower(sha256) FROM FILE WHERE lower(file_name) LIKE '%.apk';" > nsrl-apk.sha256
   ```

4. **Vérifiez** le résultat : une empreinte de 64 caractères par ligne. L'appli conserve au plus **3 000 000** empreintes (8 octets de mémoire chacune).
5. **Copiez** `nsrl-apk.sha256` sur le téléphone. Dans l'appli, ouvrez **Paramètres → Avancé → Liste NSRL (import manuel) → Importer…** et choisissez le fichier. Un nouvel import remplace le précédent, et **Retirer** le supprime.

Tout fichier texte contenant des empreintes hexadécimales de 64 caractères convient (listes simples, CSV, exports entre guillemets). Pour utiliser votre propre liste, passez plutôt par **Paramètres → Avancé → Fichiers de confiance → Importer…**.

Caractéristiques
----------------
- Impact quasi nul sur la batterie : vous ne remarquerez aucun effet sur l'autonomie
- Extrêmement rapide : il peut analyser de petits fichiers (1 Mo) en moins de 20 ms, et même de gros fichiers (40 Mo) en 1000 ms
- Économe en mémoire : avec les bases de données par défaut, il utilise moins de 120 Mo
- Analyse manuelle : permet de sélectionner /system, le stockage interne, le stockage externe et les applications installées
- Scanner en temps réel : détecte les logiciels malveillants à l'écriture ou au renommage de fichiers dans le stockage interne, et analyse les applications lors de leur installation ou mise à jour
- Entièrement hors ligne : Internet n'est utilisé que pour télécharger les bases de signatures, les fichiers ne quittent jamais votre appareil
- Mises à jour automatiques optionnelles des bases : fréquence (de 6 h à une fois par semaine) et réseau configurables (Wi-Fi uniquement par défaut, données mobiles en option), avec téléchargement seulement si le serveur a un fichier plus récent (HTTP 304)
- Persistance : redémarre automatiquement au démarrage et après une mise à jour
- Code source minuscule : il peut être audité même par quelqu'un ayant une expérience de base en programmation
- Dépendances minimales : l'application n'utilise des bibliothèques que lorsque c'est nécessaire
- Les bases de signatures peuvent être activées ou désactivées à la demande de l'utilisateur


Serveurs de bases de données et clés de signature
-------------------------------------------------
Par défaut, Asclépios AV télécharge ses bases depuis [Jdont9/HypatiaDatabases](https://github.com/Jdont9/HypatiaDatabases). Pour changer de serveur, ouvrez les Paramètres (icône d'engrenage en haut à droite de l'écran principal), puis `Réseau` → `Remplacer le serveur de base de données`. La clé de signature correspondante est appliquée automatiquement ; pour un serveur personnalisé, saisissez sa clé manuellement dans `Avancé` → `Signature utilisée pour signer la base de données`.

| Serveur (nom dans l'application) | URL | Clé de signature |
|---|---|---|
| **Serveur Principal** (par défaut, Jdont9) | https://jdont9.github.io/HypatiaDatabases/ | `B93D98077D1C` |
| Serveur Maintain Team (Codeberg) | https://maintainteam.codeberg.page/HypatiaDatabases/ | `5298C0C0C3E73288` |
| Serveur Maintain Team Miroir (GitHub) | https://maintainteam.github.io/HypatiaDatabases/ | `5298C0C0C3E73288` |
| AXP.OS | https://lav.axpos.org/db/ | `14C17E7F99EABF3F` |

Sources : [Jdont9/HypatiaDatabases](https://github.com/Jdont9/HypatiaDatabases) · [MaintainTeam/HypatiaDatabases](https://github.com/MaintainTeam/HypatiaDatabases) · [miroir Codeberg](https://codeberg.org/MaintainTeam/HypatiaDatabases)

Dépannage
---------
- **L'application plante et est très instable :**
Vérifiez d'abord si les bases de données étendues sont activées. Elles nécessitent davantage de RAM (8 Go) et peuvent parfois rendre l'application très instable.
- **Impossible de télécharger les bases de données :**
Ouvrez les Paramètres (icône d'engrenage en haut à droite de l'écran principal), puis `Remplacer le serveur de base de données` dans `Réseau`. Cela permet d'utiliser un miroir si le serveur principal est indisponible.
- **Il y a des faux positifs :**
Cela arrive occasionnellement en raison de la nature des filtres de Bloom. Si vous pensez avoir un faux positif, relancez d'abord l'analyse, ce qui le corrige parfois. S'il persiste, envoyez le fichier à [VirusTotal](https://www.virustotal.com/gui/home/upload) : il vous dira s'il s'agit réellement d'un faux positif ou d'un logiciel malveillant.

Informations sur l'APK et sécurité
----------------------------------

Les versions debug, release et nightly sont compilées par GitHub Actions. Vous pouvez comparer la somme de contrôle de l'application avec celle indiquée dans les Release Actions ou dans le fichier checksum.txt des publications.

Les versions de ce fork (Asclépios AV) sont signées avec une clé dont l'empreinte SHA-256 du certificat est :
```
6D:D9:76:DD:3E:77:AF:FE:AB:CF:03:3B:B6:AC:3E:07:B8:53:31:D1:EC:60:1F:F0:27:78:CA:EF:73:EE:C1:B6
```
Vérifiez un APK avec `apksigner verify --print-certs`. Ces versions ne mettent pas à jour l'Hypatia d'origine (identifiant d'application et clé de signature différents).

À titre indicatif, voici l'empreinte SHA de la clé de signature d'Hypatia d'origine, utilisée par les versions officielles de MaintainTeam :
```
1B:00:8D:64:BB:95:AB:47:74:D6:8B:87:F2:2B:8B:E9:A2:72:F4:92:4D:F5:20:29:D7:E6:18:38:35:D9:18:CC
```

Détails techniques
------------------
- Les bases de signatures sont au format de sérialisation d'objet BloomFilter de Guava
- Les bases de signatures ne sont pas retéléchargées si le fichier n'a pas changé sur le serveur (304 Not Modified)
- Une tâche JobScheduler optionnelle (de 6 h à une fois par semaine, une fois par jour par défaut ; Wi-Fi uniquement par défaut, données mobiles en option) vérifie la présence de bases plus récentes et les télécharge
- Les signatures sont stockées dans des BloomFilters pour une recherche en O(k)
- Les hachages MD5, SHA-1 et SHA-256 des fichiers sont calculés en un seul passage
- Le scanner en temps réel est multitâche et utilise la moitié du nombre de cœurs de l'appareil pour analyser plusieurs fichiers de manière asynchrone
- L'analyse en temps réel repose sur un FileObserver récursif
- Les analyses et les téléchargements s'exécutent sur un pool de threads dédié (sans `AsyncTask`, déprécié) ; les journaux et notifications sont toujours émis depuis le thread principal

Autorisations
-------------
- `ACCESS_NETWORK_STATE` : vérifie si un réseau est disponible avant de mettre à jour les bases.
- `FOREGROUND_SERVICE` et `FOREGROUND_SERVICE_SPECIAL_USE` : utilisées pour l'analyse en temps réel.
- `INTERNET` : télécharger et mettre à jour les bases de données.
- `MANAGE_EXTERNAL_STORAGE` : lire les fichiers malveillants pour les analyser et supprimer les fichiers infectés.
- `WRITE_EXTERNAL_STORAGE` et `READ_EXTERNAL_STORAGE` : analyser et supprimer les fichiers infectés sur les anciennes versions d'Android.
- `QUERY_ALL_PACKAGES` : analyser les applications malveillantes.
- `RECEIVE_BOOT_COMPLETED` : relancer l'application au redémarrage.
- `REQUEST_DELETE_PACKAGES` : désinstaller les applications infectées.
- `POST_NOTIFICATIONS` : afficher les notifications.
- `WAKE_LOCK` : garde le téléphone éveillé pendant l'analyse pour éviter que le processus ne soit tué.
- `ACCESIBILITY_SERVICE` : permet à l'analyseur de liens de lire l'écran et de détecter les domaines malveillants.
- `DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` : requise par Android pour la déclaration des récepteurs.

Compilation
-----------
Compiler l'application est similaire à la plupart des applications Android, mais pour synchroniser le projet dans Android Studio, vous devrez peut-être ajouter ce qui suit à [verification-metadata.xml](https://github.com/MaintainTeam/Hypatia/blob/stable/gradle/verification-metadata.xml) :
```xml
      <trusted-artifacts>
         <trust file=".*-javadoc[.]jar" regex="true"/>
         <trust file=".*-sources[.]jar" regex="true"/>
      </trusted-artifacts>
```

Objectifs
---------
- Être rapide
- Ne pas vider la batterie
- Utiliser un minimum d'autorisations
- N'utiliser des bibliothèques que lorsque c'est nécessaire

Crédits
-------
- ClamAV pour les bases de données (GPLv2)
- ESET pour des bases de données supplémentaires (BSD 2-Clause)
- Nex (@botherder) pour des bases de données supplémentaires (CC BY-SA 4.0)
- Amnesty International pour des bases de données supplémentaires (CC BY 2.0)
- Echap pour des bases de données supplémentaires (CC BY 4.0)
- MalwareBazaar pour des bases de données supplémentaires (CC0)
- RecursiveFileObserver.java (GPL-3.0-or-later) : Daniel Gultsch, ownCloud Inc., Bartek Przybylski
- GPGDetachedSignatureVerifier.java (GPL-2.0-or-later) : Federico Fissore, Arduino LLC
- Petra Mirelli pour la bannière / le graphique de présentation de l'application et divers ajustements
- @eloitor : travail sur les traductions
- Icônes : Google/Android/AOSP, licence : Apache 2.0, https://google.github.io/material-design-icons/

Traductions
-----------
- Afrikaans : Oswald van Ginkel
- Arabe : abdelbasset jabrane, ABDO GM
- Chinois (simplifié) : Sdarfeesh, Crit, 大王叫我来巡山
- Chinois (traditionnel) : 張可揚
- Croate : lukapiplica
- Tchèque : Fjuro
- Estonien : Priit Jõerüüt
- Finnois : huuhaa, Ricky Tigg
- Français : cardpuncher, Jean-Luc Tibaux, Petra Mirelli, thraex
- Hébreu : elid34
- Galicien : ghose, josé m
- Allemand : thereisnoanderson, Balthazar1234, Petra Mirelli, Ettore Atalan
- Grec : Dimitris Vagiakakos
- Indonésien : Adrien N
- Italien : Tommaso Fonda, srccrow, Petra Mirelli, Dark Space
- Japonais : honyaku
- Polonais : Marcin Mikołajczak
- Portugais (Brésil) : lucasmz
- Portugais : jontaix, inkhorn, ssantos
- Roumain : Renko
- Russe : yurtpage, q1011, Andrey
- Slovaque : Pa Di
- Espagnol : gallegonovato, Manuel-Senpai, Petra Mirelli
- Turc : cardpuncher
- Ukrainien : Fqwe1

Avis
----
- Divested Computing Group n'est pas affilié à Cisco ou à ESET
- MaintainTeam n'est pas affilié à Cisco ou à ESET
- Hypatia n'est pas sponsorisé ni approuvé par Cisco ou ESET
