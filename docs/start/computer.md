---
title: Install on a computer
guide: miso
quote: "Let's get the app open first. I'll walk you through the launcher, then we'll connect a model."
---

# Install on a computer

Neconyan runs on Windows, macOS and Linux. Download it, extract it and run the launcher. The first start needs internet access to install the files it needs.

## Download and extract

1. Open the [latest Neconyan release](https://github.com/platberlitz/Neconyan/releases/latest).
2. Download the release asset whose name ends in **-source.zip**.
3. Extract the entire archive into a folder you can write to, such as a folder inside your home directory.
4. Open the extracted Neconyan folder. Don't run the launcher from inside the ZIP preview.

Keep the folder somewhere you can find again. In a standard installation, it also holds your saved data.

## Run the launcher

=== "Windows"

    Double-click **Start.bat**. Leave the terminal window open while you use Neconyan. The first run can take longer while it installs dependencies.

=== "macOS"

    Open **Start.command**. If macOS requires permission, allow the file through the normal security prompt for the copy you downloaded from the official release.

    If it isn't executable, open a terminal in the extracted folder and run:

    ```sh
    chmod +x Start.command
    ./Start.command
    ```

=== "Linux / WSL"

    Open a terminal in the extracted folder and run:

    ```sh
    bash start.sh
    ```

    Keep the terminal open. If you use WSL on Windows, the app runs inside that environment; keep its data in a folder that environment can write to.

The browser should open automatically. If it doesn't, open this address on the computer running Neconyan:

```text
http://127.0.0.1:4433/
```

You should see Home. Next, [connect your model](connections.md).

## Install with Git instead

Git keeps track of the downloaded source and lets the launcher update a clean installation. If you already have Git installed, this is convenient for regular use.

```sh
git clone https://github.com/platberlitz/Neconyan.git
cd Neconyan
```

Then run the launcher for your system.

To update, open **Server → Updates & Restart → Check for updates**, then **Update & Restart**. This works for Git and supported source ZIP installations. Git launchers also check at startup and leave edited source alone. [Updates and backups](../help/backups.md) covers older ZIP copies and backing up first.

## Stop and restart

Return to the launcher's terminal and press ++ctrl+c++ to stop the server. Run the launcher again to restart it. Closing the browser doesn't stop a server that's still running in the terminal.

!!! taro "Taro"
    If the page says it can't connect, read the terminal error before reinstalling. It may tell you exactly what failed. Reinstalling enthusiastically is still guessing.

## Manual runtime requirements

If you manage the runtime yourself, use **Node.js 20 or later**, or a stable **Bun 1.4.0 or later**. The current launcher refuses older Bun releases, including 1.3.x. The launcher can install Bun when it needs a runtime. Don't copy a dependency folder from a different operating system; let the launcher install the appropriate files.

For a phone on the same Wi-Fi, continue with [Open it on your phone](phone.md). If installation stops with an error, collect the terminal message and check [troubleshooting](../help/troubleshooting.md).
