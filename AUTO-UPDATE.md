# Automatic daily database updates

Hypatia can now check the signature servers once a day and download a database
only when the server has a newer file (HTTP `If-Modified-Since` / `304`).

## How to use

1. Open Settings (gear icon in the toolbar) → Updates.
2. Enable **Automatic database updates**.
3. If you are already on Wi-Fi, Hypatia runs a check immediately.
4. If you are on mobile data, the first check waits for an unmetered network.
5. After that, a daily `JobScheduler` task (flex window of 6 hours, Wi-Fi only,
   battery/storage not low) repeats the same check.

Nothing is uploaded. Files never leave the device. Existing GPG signature
verification is unchanged.

## Implementation

- `DatabaseUpdateScheduler` — persists the preference, schedules/cancels jobs
- `DatabaseUpdateJobService` — runs the existing `Database.updateDatabase()`
  path, waits for downloads, reloads Bloom filters if a file changed, and
  posts a low-priority notification only when something was actually downloaded
- Restored on boot / app update via `EventReceiver` and `Hypatia.onCreate`

Uses Android `JobScheduler` (no WorkManager) so F-Droid dependency verification
and Hypatia's "minimal dependencies" rule stay intact.

## Frequency and network options

Settings (gear icon) → Updates → **Auto-update frequency and network** lets you choose:

- Frequency: every 6 h, 12 h, once a day (default), every 2 days, once a week
- Network: Wi-Fi only (default), Wi-Fi + mobile data (not roaming), any network (roaming included)

Mobile-data updates can download up to 50 MB (200 MB with extended signatures).
Changing the options reschedules the periodic job immediately.
