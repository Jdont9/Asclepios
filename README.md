> [!WARNING]
> ### This is a fork of the [original](https://github.com/Divested-Mobile/Hypatia) (and discontinued) app from DivestOS.
> ### This repository ([Jdont9/Hypatia](https://github.com/Jdont9/Hypatia)) is **Asclépios AV**, my personal fork of [MaintainTeam/Hypatia](https://github.com/MaintainTeam/Hypatia), see [Changes in this fork](#changes-in-this-fork-42).

![Banner](./fastlane/metadata/android/en-US/images/featureGraphic.png)

Asclépios AV
============
_A fork of [Hypatia](https://github.com/MaintainTeam/Hypatia), originally created by Divested Computing Group._

Overview
--------
Asclépios AV is a fork of Hypatia, the world's first FOSS malware scanner for Android. It is powered by ClamAV style signature databases.

<!-- [<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png"
     alt="Get it on F-Droid"
     height="80">](https://f-droid.org/packages/us.spotco.malwarescanner/) -->
[<img src="https://gitlab.com/IzzyOnDroid/repo/-/raw/master/assets/IzzyOnDroid.png"
     alt="Get the original Hypatia on IzzyOnDroid"
     height="80">](https://apt.izzysoft.de/packages/org.maintainteam.hypatia/)
[<img src="https://hosted.weblate.org/widget/maintainteam/hypatia/287x66-grey.png"
     alt="Translation status (original Hypatia)"
     height="66">](https://hosted.weblate.org/projects/maintainteam/hypatia/)

Changes in this fork (4.2)
--------------------------
Asclépios AV (application id `fr.jd.asclepios`) is [my personal fork](https://github.com/Jdont9/Hypatia) of [MaintainTeam/Hypatia](https://github.com/MaintainTeam/Hypatia), itself a fork of the discontinued [Divested-Mobile/Hypatia](https://github.com/Divested-Mobile/Hypatia). Signed APKs are on the [Releases page](https://github.com/Jdont9/Hypatia/releases). Compared to upstream `stable` (3.18):

- **Rename and identity:** the app is now called **Asclépios AV** with the application id `fr.jd.asclepios`, so it installs next to the original Hypatia and does not share its settings. It has a new icon, every "Hypatia" label shown in the app was renamed, the license shown in the app is corrected to AGPL-3.0 (as in `LICENSE`) and a copyleft line for this fork was added. The original attributions and credits are kept.

- **Modernisation:** removed the deprecated `AsyncTask` (scans and database downloads now run on a dedicated thread pool, with logs and notifications always posted from the main thread); an exception during a scan is now logged instead of crashing the app.
- **Android 16 target:** `targetSdk` raised from 34 to 36, with edge-to-edge window insets handling, removal of the `onBackPressed()` override (predictive back) and the `PROPERTY_SPECIAL_USE_FGS_SUBTYPE` declaration on both foreground services.
- **Rotation / large screens:** the portrait lock is removed and configuration changes (rotation, resizing, folding) no longer recreate the main activity, so the log is preserved.
- **Translations:** complete French translation (the disclaimer, database server names, link scanner and notification strings were missing), notification texts (`Domain:` / `File:`) and service labels moved to translatable resources, and the Weblate updates from upstream PR #98 (bg, de, et, fi, pl, ro, ru) merged.
- **Link scanner:** the domain database is now loaded automatically (after GPG signature verification) when the link scanner needs it, instead of depending on the realtime scanner or a manual scan (based on upstream PR #94).
- **Database availability after a cold start:** the app now restores its database list on startup, so manual scans and the link scanner no longer report "no database" while the files are already on the device (based on a fix from upstream PR #101).
- **Root scan:** a new "Deep scan (root)" menu option hashes /system, /vendor, /product, /data (including other apps' private data) and the other system partitions through a root shell (`su`), using the device's own `md5sum`, `sha1sum` and `sha256sum`. Since Android 11 apps only see their own data in `/data/data`, so the shell is started with `su --mount-master` (global mount namespace, like SD Maid does), falling back to plain `su` with a warning. Nothing is installed, and no dependency is added. The system / apps / internal storage options keep working on their own (without root, or if root is refused); when the root scan succeeds they are skipped since it already covers them. Matches are reported with the usual notifications, but deleting a file in a protected location from the notification is not possible without root.
- **New and updated apps:** while the realtime scanner is running, the APKs of apps being installed or updated are scanned automatically.
- **Database sanity checks:** downloads are rejected when empty or truncated (the previous working file is kept), empty databases are refused at load time, and a warning is shown when the built-in test signatures are missing.
- **Release workflow:** pushing a `v*` tag (for example `v4.2`) now builds, signs and publishes a GitHub release automatically from this repository, instead of MaintainTeam's.
- **Documentation:** the French README was rewritten to match the English one.

Not merged from upstream: the UI redesign of PR #101 (scan progress card and threat list), which the maintainers asked to be submitted separately.

Features
--------
- Near zero battery impact: you'll never notice any impact on battery at all
- Extremely fast: it can scan small files (1MB) in <20ms, and even large files (40MB) in 1000ms.
- Memory efficient: with the default databases enabled it uses under 120MB.
- Regular scan: allowing selection of /system, internal storage, external storage, and installed apps
- Realtime scanner: can detect malware in realtime on write/rename in internal storage, and scans apps as they are installed or updated
- Completely offline: Internet is only used to download signature databases, files will never ever leave your device
- Optional automatic database updates: once a day, Wi-Fi only, downloads only if the server has a newer file (HTTP 304)
- Persistence: will automatically restart on boot/update
- Tiny codebase: coming in at under 1000 sloc, it can be audited by even someone with basic programming experience
- Minimal dependencies: the app only uses libraries when necessary
- Signature databases can be enabled/disabled at the users demand


Troubleshooting
------------------
- **The app crashes and is very buggy:**
The first thing to check is if you have extended databases enabled. Extended databases require more RAM (8 GB), and can occasionally cause the app to be very buggy.
- **Unable to download databases:**
If this occurs, try tapping the ellipsis in the top right of the main screen and tap `Database server override`. This uses a mirror database in case the main database is down.
- **There are false positives:**
This occasionally occurs due to the nature of bloom filters. If you believe there is a false positive, first, rescan. This will sometimes fix the false positive. And if this still returns a false positive, scan the file to [VirusTotal](https://www.virustotal.com/gui/home/upload), and this will tell you if you truly have a false positive or rather some malware. 

APK Info & Security
--------------------

Both debug, release and nightly versions built by GitHub Actions. You can check checksum notice in Release Actions or/and checksum.txt in releases to compare with Application's

Releases of this fork (Asclépios AV) are signed with a key whose SHA-256 certificate fingerprint is:
```
6D:D9:76:DD:3E:77:AF:FE:AB:CF:03:3B:B6:AC:3E:07:B8:53:31:D1:EC:60:1F:F0:27:78:CA:EF:73:EE:C1:B6
```
Check an APK with `apksigner verify --print-certs`. These releases do not update the original Hypatia (different application id and signing key).

For reference, this is the SHA fingerprint of the signing key of the original Hypatia, used by MaintainTeam's official releases:
```
1B:00:8D:64:BB:95:AB:47:74:D6:8B:87:F2:2B:8B:E9:A2:72:F4:92:4D:F5:20:29:D7:E6:18:38:35:D9:18:CC
```

Technical Details
------------------
- Signature databases are serialized Guava BloomFilter object format
- Signature databases will not be redownloaded if the file hasn't changed on the server (304 not modified)
- Optional daily JobScheduler task (Wi-Fi / unmetered only) checks for newer databases and downloads them when present
- Signatures are stored using BloomFilters for O(k) lookup
- Files have their MD5/SHA-1/SHA-256 hashes calculated in one pass
- Realtime scanner is multithreaded and will use half of the device's core count for scanning multiple files asynchronously
- Realtime scanning powered by a recursive FileObserver
- Scans and downloads run on a dedicated thread pool (no deprecated `AsyncTask`); logs and notifications are always emitted from the main thread

Permissions
-----------------
- `ACCESS_NETWORK_STATE`: Checks if a network is available before updating databases.
- `FOREGROUND_SERVICE` and `FOREGROUND_SERVICE_SPECIAL_USE`: Used for realtime scanning.
- `INTERNET`: Download and update databases.
- `MANAGE_EXTERNAL_STORAGE`: Used for reading malicious files for scanning, and deleting infected files.
- `WRITE_EXTERNAL_STORAGE` and `READ_EXTERNAL_STORAGE`: Used for scanning and removing infected files on older Android versions.
- `QUERY_ALL_PACKAGES`: Used for scanning malicious apps.
- `RECEIVE_BOOT_COMPLETED`: Restart the app on reboot.
- `REQUEST_DELETE_PACKAGES`: Used for removing infected apps.
- `POST_NOTIFICATIONS`: Notifications.
- `WAKE_LOCK`: Keeps phone awake while scanning to prevent the process from being killed.
- `ACCESIBILITY_SERVICE`: Used to allow the link scanner to read the screen and check for malicious domains.
- `DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`: Required for receiver declarations in Android.

Building
-----
Building the app is simliar to most android apps, but if you would like to sync the app in Android Studio, you might need to add the following to [metadata-verification.xml](https://github.com/MaintainTeam/Hypatia/blob/stable/gradle/verification-metadata.xml):
```xml
      <trusted-artifacts>
         <trust file=".*-javadoc[.]jar" regex="true"/>
         <trust file=".*-sources[.]jar" regex="true"/>
      </trusted-artifacts>
```

Planned Updates
----------------
In order to view the immediate roadmap, please check out the [milestones](https://github.com/MaintainTeam/Hypatia/milestones). From here, you can gauge the time untill the next release. 😀
- Option to scan on access
- Option to let 3rd-party apps invoke scans
- Testing
- Better GUI
- Translations

Goals
-----
- Be fast
- Don't eat batteries
- Use minimal permissions
- Use libraries only when necessary

Credits
-------
- ClamAV for the databases (GPLv2)
- ESET for extra databases (BSD 2-Clause)
- Nex (@botherder) for extra databases (CC BY-SA 4.0)
- Amnesty International for extra databases (CC BY 2.0)
- Echap for extra databases (CC BY 4.0)
- MalwareBazaar for extra databases (CC0)
- RecursiveFileObserver.java (GPL-3.0-or-later): Daniel Gultsch, ownCloud Inc., Bartek Przybylski
- GPGDetachedSignatureVerifier.java (GPL-2.0-or-later): Federico Fissore, Arduino LLC
- Petra Mirelli for the app banner/feature graphic and various tweaks.
- @eloitor: Translations work
- Icons: Google/Android/AOSP, License: Apache 2.0, https://google.github.io/material-design-icons/

Translations
------------
- Afrikaans: Oswald van Ginkel
- Arabic: abdelbasset jabrane, ABDO GM
- Chinese (Simplified): Sdarfeesh, Crit, 大王叫我来巡山
- Chinese (Traditional Han script): 張可揚
- Croatian: lukapiplica
- Czech: Fjuro
- Estonian: Priit Jõerüüt
- Finnish: huuhaa, Ricky Tigg
- French: cardpuncher, Jean-Luc Tibaux, Petra Mirelli, thraex
- Hebrew: elid34
- Galician: ghose, josé m
- German: thereisnoanderson, Balthazar1234, Petra Mirelli, Ettore Atalan
- Greek: Dimitris Vagiakakos
- Indonesian: Adrien N
- Italian: Tommaso Fonda, srccrow, Petra Mirelli, Dark Space
- Japanese: honyaku
- Polish: Marcin Mikołajczak
- Portuguese (Brazil): lucasmz
- Portuguese: jontaix, inkhorn, ssantos
- Romanian: Renko
- Russian: yurtpage, q1011, Andrey
- Slovak: Pa Di
- Spanish: gallegonovato, Manuel-Senpai, Petra Mirelli
- Turkish: cardpuncher
- Ukrainian: Fqwe1

Notices
-------
- Divested Computing Group is not affiliated with Cisco or ESET
- MaintainTeam is not affiliated with Cisco or ESET
- Hypatia is not sponsored or endorsed by Cisco or ESET
