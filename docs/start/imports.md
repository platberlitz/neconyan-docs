---
title: Bring your old data
guide: miso
quote: "Bring your characters and lore, and keep a backup while we check the import. Taro will ask where it is."
---

# Bring your old data

Neconyan can use compatible character cards, chats, lorebooks, personas and presets from the SillyTavern family. You can import individual files or move selected libraries from a folder or backup ZIP.

Make a backup of both the original app and any Neconyan data you already care about. A matching imported file can replace the copy in the selected library.

## Import a character card

Open **Characters** and use **Import**. Supported card formats include character PNG, JSON, YAML, CharX and BYAF files. You can choose several files together.

A character PNG contains hidden character data as well as a picture. An ordinary image isn't automatically a complete card. Review any replacement choice before overwriting an existing character.

Cards don't contain your whole setup. Chats, connection keys, account settings and extension configuration need their own transfer. BYAF imports can include additional scenario and image content, but don't assume every card format carries it.

## Bring chats from another installation

Import or select the source character first. In **Characters → Import**, use **Bring your chats too**, then **Import chat files**. The corresponding action is also available in **Chat History → Import from another instance → Import Chat**. Character chat imports accept JSON or JSONL files, up to 64 files and 64 MiB in total per batch. JSONL files can be selected in the Android file picker too.

If you're bringing a chat from a separate installation, explicitly tick **Import as new instance**. It starts unchecked. Ordinary import keeps the existing origin checks; a refused import isn't silently converted into a new instance.

Adoption creates a new character instance and its own chat folder, even when the character name matches an existing one. It keeps the existing character and history intact. Imported message text, swipes and reasoning are retained, but the new instance doesn't inherit the source installation's identity, old branch or checkpoint links, or Mewmory state.

Retry with the same source files and the explicit option if the operation is interrupted. Neconyan can resume the saved adoption rather than create another duplicate. Direct adoption isn't available for group chats; you can select a character to adopt exported messages into a new character instance instead.

## Import selected libraries

Open **Settings → System & Device → Import & Restore**. Choose a compatible source folder or backup ZIP, then select what you want:

| Selected library | What it brings |
| --- | --- |
| Chats | Saved chats, groups, group definitions and attachments |
| Personas | Persona avatars, names and descriptions |
| Character cards | The selected source's character library |
| Lorebooks | Lorebooks and their saved history |

All four are selected initially. Clear anything you don't want to import. Other account preferences, connection keys, presets, themes and bookkeeping files aren't included in this selected-library import. Move other supported items through their own import controls.

For a folder import, the path must exist on the machine running Neconyan. A folder on the phone visiting a remote server isn't a server-side folder. Use a ZIP upload when you need to send files from the visiting device.

## Read the result before reloading

Import work is saved on the server, so closing the page doesn't automatically cancel accepted work. Return to Import & Restore and use **Choose a saved account import** to recover its status or report. A ZIP import may need you to select the original ZIP again.

After reinstalling or reconnecting, Neconyan checks whether the server still has the retained ZIP before resuming. An old browser record alone doesn't mean the archive is still available. If asked, select the original archive again and follow the current import status rather than starting several copies.

The report separates deliberately excluded files from damaged files. Supported damaged items can be skipped while the remaining selected data imports. Use **Download skipped-files report** to keep the details, then **Reload to use the imported data** when you're ready.

A completely unreadable archive or a fatal import error can still stop the operation. To recover a damaged card or lorebook, re-export it from the original app and try that file again.

!!! taro "Taro"
    'Skipped' isn't automatically 'broken'. A theme you didn't select and a damaged lorebook are different outcomes. The report separates them so you don't have to guess.

## Extensions need a separate check

**Sync Extensions** is separate from library import. Neconyan already includes several tools that used to be separate extensions; an older matching copy can be retained but inactive. Check **Extensions → Manage extensions** before enabling anything extra.

Third-party extensions may depend on a different app version or layout. Bring them over deliberately, one at a time, and confirm the basic chat still works.

## After the import

Open a few characters, load an old chat, inspect a persona and check one lorebook. Confirm that your active model connection still uses the settings you intend. Keep the source backup until you've checked the pieces you actually use.

Never point two different apps at the same live data folder. Import a copy instead. See [Updates and backups](../help/backups.md) for the difference between an account backup and an individual export.
