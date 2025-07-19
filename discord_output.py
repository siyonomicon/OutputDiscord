import torch
import numpy as np
from PIL import Image
import discord
import asyncio
import tempfile
import os
import nest_asyncio

nest_asyncio.apply()

class DiscordImageUpload:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", ),
                "bot_token": ("STRING", {"default": ""}),
                "channel_id": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "upload_image"
    OUTPUT_NODE = True
    CATEGORY = "Discord"

    def upload_image(self, image, bot_token, channel_id):
        if not bot_token or not channel_id:
            print("Discord bot token or channel ID is not set. Image will not be uploaded.")
            return ()

        # Loop through the batch of images
        for single_image_tensor in image:
            # The tensor from VAE Decode should be (H, W, C).
            # The error indicates it might have extra dimensions like (1, 1, H, W).
            # We'll remove any leading singleton dimensions to be safe.
            while len(single_image_tensor.shape) > 3:
                single_image_tensor = single_image_tensor.squeeze(0)

            # Convert tensor to PIL image
            i = 255. * single_image_tensor.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            # Save image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
                img.save(tmpfile, 'PNG')
                tmpfile_path = tmpfile.name

            # Run the async upload function
            try:
                asyncio.run(self.send_discord_file(bot_token, channel_id, tmpfile_path))
            finally:
                os.remove(tmpfile_path) # Ensure cleanup

        return ()

    async def send_discord_file(self, token, channel_id, file_path):
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            try:
                channel = client.get_channel(int(channel_id))
                if channel:
                    await channel.send(file=discord.File(file_path))
                    print("Image uploaded successfully to Discord.")
                else:
                    print(f"Could not find channel with ID: {channel_id}")
            except Exception as e:
                print(f"Failed to upload image to Discord: {e}")
            finally:
                await client.close()

        await client.start(token)

class DiscordVideoUpload:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {"default": ""}),
                "bot_token": ("STRING", {"default": ""}),
                "channel_id": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "upload_video"
    OUTPUT_NODE = True
    CATEGORY = "Discord"

    def upload_video(self, video_path, bot_token, channel_id):
        if not bot_token or not channel_id:
            print("Discord bot token or channel ID is not set. Video will not be uploaded.")
            return ()

        if not os.path.exists(video_path):
            print(f"Video file not found at path: {video_path}")
            return ()

        # Run the async upload function
        asyncio.run(self.send_discord_file(bot_token, channel_id, video_path))

        return ()

    async def send_discord_file(self, token, channel_id, file_path):
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            try:
                channel = client.get_channel(int(channel_id))
                if channel:
                    await channel.send(file=discord.File(file_path))
                    print("Video uploaded successfully to Discord.")
                else:
                    print(f"Could not find channel with ID: {channel_id}")
            except Exception as e:
                print(f"Failed to upload video to Discord: {e}")
            finally:
                await client.close()

        await client.start(token)