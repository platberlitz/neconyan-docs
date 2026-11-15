---
title: Open it on your phone
guide: taro
quote: "The phone needs the address of the computer running Neconyan. 'Localhost' on the phone means the phone. Annoyingly literal, but correct."
---

# Open it on your phone

You can install Neconyan on an iPhone or [Android phone](android.md), or open it in a browser while it runs on your computer.

For browser access, this guide uses the **same trusted home network**. The computer must stay awake with Neconyan running.

## Use the standalone iPhone app

The project now includes a standalone iPhone app. It bundles Node.js, the server and the interface, so your chats and settings live on the phone and no computer needs to run Neconyan. It needs **iOS 17 or newer** and isn't an App Store build. You sideload it, which means installing it yourself, with a tool such as [iloader](https://github.com/nab138/iloader), which signs it with your Apple account.

With a free Apple account, the app has to be re-signed every seven days, and you can have three sideloaded apps. To keep your chats, install a newer IPA over the old one with the same Apple account. Deleting the app deletes your chats with it, so export an account backup first if you're changing tools.

Download the file ending in **-ios-unsigned.ipa** from the [release page](https://github.com/platberlitz/Neconyan/releases/latest). If your chosen release has no IPA, use the browser setup below.

Imports keep going when you switch apps or lock the phone. Pick the backup with the app's **Import Backup ZIP** button, confirm, and the server takes it from there. Allow about twice the backup's size in free space while it's copied in.

Replies keep going the same way. If you leave mid-reply, the page plays a silent sound until the reply is written, saved and its after-reply Agents have run. You might see 'Neconyan is finishing a reply' on the lock screen, and music from another app can pause until it's done. iOS can still close the app when the phone runs short of memory. [The iPhone setup notes](https://github.com/platberlitz/Neconyan/blob/staging/ios/README.md) cover the build and its limits.

If two starts in a row don't finish, the next load offers a safe start. On iPhone and iPad it turns low-memory mode on automatically unless you've set it off, and that setting is saved until you change it. The button then reads **Start without low-memory mode**. **Read crash report** works before the app loads. [Something went wrong](../help/troubleshooting.md#the-page-wont-open) lists the other buttons.

If the page stops, a page load fails or the local sign-in doesn't finish, the app stops retrying by itself and shows a recovery screen with what happened. **Try again** starts the server and loads the page again. **Share startup log** prepares a report you can send or save. Both buttons stay available when you come back from another app, so you can look something up without losing the screen. The startup log survives relaunches. It records the last startup step, timings, the device and recent activity, and hides credentials Neconyan recognises. You can share it even when the local server never started. The shared report ends with the last part of the server log. The app also clears a data folder lock left behind by a run iOS closed.

The documented build checks use Apple's iPhone simulator. They don't show that every feature works on a physical iPhone.

## Allow connections from your network

1. Stop Neconyan on the computer.
2. Open its **config.yaml** in a text editor. Use the actual configuration beside your installation, not the template inside the default folder.
3. Change the existing settings below, keeping the indentation. Replace the example username and password with your own.

```yaml
listen: true
basicAuthMode: true
basicAuthUser:
  username: 'your-chosen-name'
  password: 'replace-with-your-own-long-password'
```

These are selected settings, not a replacement for the whole file. Don't add a second copy of a key that's already present. Save, then start Neconyan again.

If your firewall asks, allow the connection on your private home network.

## Find the computer's address

Find its local IPv4 address in your network settings. It usually begins with **192.168.**, **10.** or **172.16.** through **172.31.**.

=== "Windows"

    In a terminal, run:

    ```bat
    ipconfig
    ```

    Look for the IPv4 address under the Wi-Fi or Ethernet connection you're using.

=== "macOS"

    Open your Wi-Fi or Ethernet connection details in System Settings and find the IP address.

=== "Linux"

    In a terminal, run:

    ```sh
    hostname -I
    ```

    Use the address for your home network, not one for a container or VPN connection.

On the phone, open the address below, replacing the example IP with the computer's address:

```text
http://192.168.1.42:4433/
```

Sign in with the credentials you set. Your existing chats should be there because you're opening the same server.

## If access is forbidden

The allow-list is the list of addresses that may connect. By default it includes common **192.168.** and **172.16.-172.31.** home networks. If your network uses **10.**, add its range to the existing list in the configuration and keep the other entries:

```yaml
whitelist:
  - ::1
  - 127.0.0.1
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 10.0.0.0/8
```

Restart the server after changing the configuration. Guest Wi-Fi can stop devices seeing one another. Use a network that lets the phone reach the computer.

## Add it to your Home Screen

On iPhone, open Neconyan in Safari, open Share and choose **Add to Home Screen**. On Android, use the browser's install or Home Screen option when available. This gives you an app-like window. It still needs the server to be running.

On iPhone Safari, turning **Movable panels** off no longer leaves an empty band above the keyboard. The Home Screen app reserves space for the home bar once, rather than leaving a doubled gap. On Android browsers, returning from another app keeps the composer inside the visible screen, including when **Movable panels** is on.

Some app-install and browser features require HTTPS, a secure web address. Plain HTTP on a home network may not offer every browser feature.

## Notifications {#notifications}

Open **Settings → System & Device → Notifications** and turn on **Push notifications**. It's off by default, belongs to this device and account, and asks for permission when you turn it on.

In a browser, notifications need HTTPS or localhost, browser push support and a service worker, a script the browser runs in the background. The plain home-network HTTP address in this guide doesn't provide them. On iPhone and iPad, an HTTPS Neconyan site also needs to be added to the Home Screen and opened there. The standalone iPhone app uses native notifications instead. Allow them when asked and keep its local server running. Message previews can appear on the lock screen. If the system blocks them, allow notifications in iOS settings, then turn the switch on again. [Conversation's device notifications](../workspace/conversation.md#notifications) covers the shared limits.

## Keep an Android browser tab open

In an Android browser, **Settings → System & Device → Leaving the tab** offers **Stay open in the background**. It's off by default and applies to that device only. Turning it on plays a sound too quiet to hear while Neconyan is hidden, so Chrome is less likely to unload the tab when you switch away.

It uses more battery, shows a media notification and can pause music in other apps. Start with a short reply to see how your phone's battery manager reacts before relying on it for a long scene. The switch is hidden in the Android app, which manages its own background work.

## Away from home

The local address above won't work from mobile data. Use HTTPS hosting that requires a sign-in, or a private network connection to your server. Don't open the example HTTP port directly to the internet. This local-network setup doesn't configure encrypted public hosting.

If the page loads but replies fail, your phone connection is working. Continue with [model connection troubleshooting](../help/troubleshooting.md#the-page-opens-but-the-model-wont-reply).
