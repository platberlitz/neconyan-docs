---
title: Install on Android
guide: miso
quote: "Yes, the Android app runs Neconyan on the phone itself. Your computer can have the evening off."
---

# Install on Android

The official Android app includes the Neconyan server. You can keep your characters, chats and settings on the phone without a computer or Termux. You'll still need a model connection for generated replies.

## Before you install

- Android **11 or later**.
- At least **2 GiB of free space**, with more for a large library or image collection.
- **Android System WebView 124 or later**. WebView is the Android component that displays the app's interface. Update it through your device's app store if necessary.
- An internet connection for the download and for any online model provider you choose.

## Install the APK

1. Visit the [latest release](https://github.com/platberlitz/Neconyan/releases/latest) on your phone.
2. Download the file ending in **-android-arm64.apk** for a normal modern phone. The x86_64 build is mainly for compatible emulators and devices.
3. Open the download. Android may ask you to allow installation from the browser or file app you used.
4. Install Neconyan, open it and wait for the first setup to finish.
5. Follow [Connect a model](connections.md), then open [your first chat](first-chat.md).

For replies, [connect an online provider or a local model service](connections.md).

## While it's running

Neconyan shows an ongoing notification with controls to return to the app or stop the server. If you want work to continue while the screen is off, check the app's background and battery settings in Android.

Accepted server work can continue after the interface closes, but Android can still stop the entire app. If a provider request was interrupted and its outcome is unknown, don't assume it is free to repeat. Check the task's status and your provider before retrying a costly operation.

!!! taro "Taro"
    A battery manager can be extremely good at preventing background work. It has, unfortunately, decided that your background work also counts.

## If the app won't open

Neconyan watches its local server while it starts. If the server stops, for example because the phone ran out of memory while loading a large library, the app starts it again once in **safe mode**. Safe mode pauses background memory updates and automatic Conversation messages, and any task that was interrupted waits for you to retry it. Your chats load as normal, and the next time you open the app it starts normally again.

If the server still can't start, the app shows a recovery screen:

- **Try again** starts the server again.
- **Save a backup of my data** saves a ZIP of your account folder: characters, chats, personas, lorebooks and settings. It works even though the server isn't running. Saved API keys are left out unless you choose **Include API keys**; keep that file private if you do.
- **Copy details for a bug report** copies the reason Android gave for stopping the server and the last lines of its log. From 1.2.4 it also includes the native server's stack size. Paste the full report into a [GitHub issue](https://github.com/platberlitz/Neconyan/issues).
- **Close Neconyan** stops the app.

To bring the backup into another installation, such as Termux or a computer, open **Settings > System & Device > Import & Restore** there and choose **Import Backup ZIP**. It brings across chats, personas, character cards and lorebooks; other settings, presets and API keys stay in the ZIP and aren't applied. Save the backup before you consider uninstalling; uninstalling removes the app's data.

### If sending or regenerating crashes

A report saying **signal 11** means the native server crashed. It doesn't prove your chat is damaged or that the phone ran out of memory. Keep the chat and save a backup before trying changes.

If a blank chat works but an existing chat crashes, include that detail with the full copied report, your model and provider, and whether sending, regenerating or both trigger it. I need that distinction to investigate the crash. Install the latest APK over the existing app; you don't need to delete the old chat to update.

## Update without losing your library

Install the newer official APK **over the existing app**. This preserves the app's private data when Android accepts it as an update. Export a backup before updating, especially before changing devices.

Uninstalling the app removes its private data. If Android refuses an update because the package's signature doesn't match, back up before considering an uninstall. Don't treat an uninstall as a harmless troubleshooting step.

The native Android export bridge accepts files up to **1 GiB**. For a very large collection, use smaller individual exports or another supported transfer route rather than relying on one oversized download.

## Prefer Termux?

Termux is an alternative installation, separate from the official app. Get it from [F-Droid](https://f-droid.org/packages/com.termux/) or [Termux's official releases](https://github.com/termux/termux-app/releases), then run:

```sh
pkg update && pkg upgrade -y
pkg install -y git
git clone --depth 1 https://github.com/platberlitz/Neconyan.git ~/Neconyan
cd ~/Neconyan
bash start.sh
```

Keep the project under Termux's home directory. Shared storage such as `/sdcard` doesn't support all the file links required by the installation. Leave Termux running; Neconyan asks Android for a wake lock at startup to help prevent sleep. Press ++ctrl+c++ there to stop the server.

Some phones report file times wrongly. Neconyan checks the data folder at startup and switches on a compatibility mode when needed; that data then has to be started with Node.js, not Bun. If you used the Termux import recovery, the usual `bash start.sh` carries on with the saved recovery folder on port 5534. The [Termux import recovery guide](https://github.com/platberlitz/Neconyan/blob/staging/docs/termux-import-recovery.md) has the details.

If the server is already on a computer, you can simply [open that installation in your phone's browser](phone.md) instead. Its data stays on the computer.
