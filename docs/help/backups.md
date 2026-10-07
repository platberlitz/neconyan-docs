---
title: Updates and backups
guide: taro
quote: "A backup is a copy you can recover from. A button labelled History is useful, but it does not become a backup through optimism."
---

# Updates and backups

Keep an independent copy before updating, importing a large library or making broad edits. Different exports cover different things.

## Choose the right export

| Export or copy | Useful for | Doesn't automatically include |
| --- | --- | --- |
| Character card | Moving a character definition | All chats, gallery media and account settings |
| Chat export | Keeping a conversation | The whole account or every related tool setting |
| Notebook export | Portable Markdown notes and files | Revision history, AI permissions and lore bindings |
| Mewmory export | Its supported memory records | Connection keys or deleted chat sources |
| Chat Archive organisation | Folders, collections and saved views | Chat contents |
| Account backup | A broader account archive | Main secrets unless the server allows key exposure |
| Stopped-server data/config copy | Recovering a self-managed installation | A guarantee that another app can use the same files |

Read an export's scope before relying on it. Private content and, depending on server settings, credentials can be present in an archive. Keep backups somewhere you control.

## Download an account backup

Open **Settings → Cache & Account → Account Settings → Account**, then use **Download Backup**. The accepted backup runs as saved server work, so closing the page doesn't automatically stop it.

Return to the account controls and use **Choose a saved account backup**, then **Download saved backup**, to recover completed work. **Stop backup** requests cancellation.

Store the downloaded archive on another device or independent storage service, where a disk failure or app uninstall won't remove it.

## Back up a self-managed installation

Stop Neconyan before copying its live data. In a standard setup, preserve the **data** folder and your actual **config.yaml**. If you configured a different data root, copy that location instead.

Keep the old copy until the restored installation opens correctly and you can inspect the chats, characters and other work you care about. Never run two apps against the same writable data folder.

## Update a Git installation

The launcher checks for updates when a Git installation starts. Local source edits or disabled automatic updating can stop that process. Read the terminal output if it declines to update rather than forcing a reset over your own changes.

After updating, reload the browser and check a saved chat and your active connection. Included tools update with the app; separately installed extensions have their own updates and compatibility.

## Update a ZIP installation

1. Back up, then stop the old Neconyan server.
2. Download and extract the newer official source release into a new folder.
3. Copy your data and any changed configuration into the new installation, preserving the originals.
4. Start the new launcher and check the result.
5. Keep the old folder until you've confirmed the new copy contains your work.

Don't overwrite a running installation with a mixture of old and new source files.

## Update Android

Install the new official APK over the existing app. Export before updating or moving devices. **Uninstalling removes the app's private data.** See [Android installation](../start/android.md) for the supported versions and large-export limit.

## Restore deliberately

[Import & Restore](../start/imports.md) selects particular libraries from a compatible folder or ZIP. It doesn't blindly restore every setting in an account archive. Individual formats have their own import controls.

Time Machine snapshots, notebook history and Chat Archive organisation are helpful recovery tools with narrower scopes. Keep an independent backup even when you use them.
