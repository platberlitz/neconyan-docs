---
title: Open it on your phone
guide: taro
quote: "The phone needs the address of the computer running Neconyan. 'Localhost' on the phone means the phone. Annoyingly literal, but correct."
---

# Open it on your phone

An iPhone or iPad can use Neconyan through a browser while the server runs on another computer or host. Android also supports this setup, or you can [run the Android app itself](android.md).

This guide covers a phone and computer on the **same trusted home network**. Both must be connected, and the computer must stay awake with Neconyan running.

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

These are selected settings, not a replacement for the entire file. Don't add a second copy of a key that's already present. Save, then start Neconyan again.

If your firewall asks, allow the connection on your private home network.

## Find the computer's address

Find its local IPv4 address in your network settings. It commonly begins with **192.168.**, **10.** or **172.16.** through **172.31.**.

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

    Use the address for your home network, rather than a container or VPN connection.

On the phone, open the address below, replacing the example IP with the computer's address:

```text
http://192.168.1.42:4433/
```

Sign in with the credentials you set. Your existing chats should be there because you're opening the same server.

## If access is forbidden

The default address allow-list includes common **192.168.** and **172.16.-172.31.** home networks. If your actual network uses **10.**, add its range to the existing list in the configuration, retaining the other entries:

```yaml
whitelist:
  - ::1
  - 127.0.0.1
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 10.0.0.0/8
```

Restart the server after changing the configuration. Guest Wi-Fi can isolate devices from one another; use a network that permits the phone to reach the computer.

## Add it to your Home Screen

On iPhone, open Neconyan in Safari, open Share and choose **Add to Home Screen**. On Android, use the browser's install or Home Screen option when available. This gives you an app-like window; it still needs the server to be running.

Some app-install and browser features require HTTPS, a secure web address. Plain HTTP on a home network may not expose every browser feature.

## Away from home

The local address above won't work from mobile data. Use an authenticated HTTPS hosting setup or a private network connection to your server. Don't expose the example HTTP port directly to the internet: this local-network recipe doesn't configure encrypted public hosting.

If the page loads but replies fail, your phone connection is working. Continue with [model connection troubleshooting](../help/troubleshooting.md#the-page-opens-but-the-model-wont-reply).
