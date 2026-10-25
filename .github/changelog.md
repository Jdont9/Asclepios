Personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## Features
- The link scanner now loads the domain database by itself (after GPG verification).
- Rotation and large screens are supported (no more portrait lock).
- New "Deep scan (root)" option: scans protected locations such as /data/data through `su`.
- Newly installed or updated apps are scanned automatically while the realtime scanner runs.
- Database sanity checks: empty or truncated downloads are rejected, empty databases are refused, and a warning is shown when the test signatures are missing.

## Bug Fixes
- Fixed "no database available" after a cold start even though the databases were already downloaded.
- Fixed untranslated strings (French) and hardcoded notification texts.

## Development Updates
- Removed the deprecated `AsyncTask`.
- `targetSdk` raised to 36 (edge-to-edge, predictive back, foreground service declarations).
- Release workflow now builds and publishes from this repository.
- Updated translations (bg, de, et, fi, pl, ro, ru, fr).
