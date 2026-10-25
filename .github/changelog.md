Personal fork of MaintainTeam/Hypatia, see the README for the full list of changes.

## Features
- The link scanner now loads the domain database by itself (after GPG verification).
- Rotation and large screens are supported (no more portrait lock).

## Bug Fixes
- Fixed "no database available" after a cold start even though the databases were already downloaded.
- Fixed untranslated strings (French) and hardcoded notification texts.

## Development Updates
- Removed the deprecated `AsyncTask`.
- `targetSdk` raised to 36 (edge-to-edge, predictive back, foreground service declarations).
- Release workflow now builds and publishes from this repository.
- Updated translations (bg, de, et, fi, pl, ro, ru, fr).
