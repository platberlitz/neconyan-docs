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

Keep the project under Termux's home directory. Shared storage such as `/sdcard` doesn't support all the file links required by the installation. Leave Termux running; its wake lock can help prevent sleep. Press ++ctrl+c++ there to stop the server.

If the server is already on a computer, you can simply [open that installation in your phone's browser](phone.md) instead. Its data stays on the computer.
