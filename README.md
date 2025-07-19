# ComfyUI Discord Output Nodes

![](https://github.com/siyonomicon/OutputDiscord/blob/main/images/screenshot.png?raw=true)

This repository contains two custom nodes for ComfyUI that allow you to upload images and videos directly to a Discord channel.

## Features

- **Discord Image Upload**: Uploads an image directly from a VAE Decode node (or any other image source) to a specified Discord channel.
- **Discord Video Upload**: Uploads a video from a local file path to a specified Discord channel. This is useful for workflows that generate video files.

## Installation

1.  **Clone or download this repository** into your `ComfyUI/custom_nodes/` directory.
2.  **Install the required Python packages.** Open a terminal or command prompt, navigate to your ComfyUI installation directory, activate your virtual environment, and run:

    ```bash
    pip install -r custom_nodes/OutputDiscord/requirements.txt
    ```

    This will install the necessary `discord.py` and `nest_asyncio` libraries.

3.  **Restart ComfyUI.**

## Configuration

These nodes require a Discord bot token and a channel ID to function.

### 1. Create a Discord Bot and Get a Token

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications) and click "New Application".
2.  Give your application a name and click "Create".
3.  Go to the "Bot" tab and click "Add Bot".
4.  Under the bot's username, click "Reset Token" (or "Copy Token" if you've already saved it) to get your bot token. **Treat this token like a password and never share it publicly.**

### 2. Invite the Bot to Your Server

1.  Go to the "OAuth2" -> "URL Generator" tab.
2.  Select the `bot` scope.
3.  In the "Bot Permissions" section that appears, select `Send Messages` and `Attach Files`.
4.  Copy the generated URL at the bottom of the page, paste it into your browser, and invite the bot to your desired server.

### 3. Get the Channel ID

1.  In your Discord client, enable Developer Mode (User Settings > Advanced > Developer Mode).
2.  Right-click on the text channel you want the bot to upload files to and select "Copy Channel ID".

## Usage

After restarting ComfyUI, you will find two new nodes in the "Discord" category:

### Discord Image Upload

-   **image**: Connect the `IMAGE` output from a node like `VAE Decode` to this input.
-   **bot_token**: Paste your Discord bot token here.
-   **channel_id**: Paste the ID of the channel you want to upload the image to.

### Discord Video Upload

-   **video_path**: Connect a `STRING` output containing the absolute file path to your video file. This can be from a node like `Select Filename` from the `comfyui-videohelpersuite`.
-   **bot_token**: Paste your Discord bot token here.
-   **channel_id**: Paste the ID of the channel you want to upload the video to.

**Note:** The bot will only be online for the brief moment it takes to upload the file. It is normal for it to appear as "Offline" in your Discord server.
