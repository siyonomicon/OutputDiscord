from .discord_output import DiscordImageUpload, DiscordVideoUpload

NODE_CLASS_MAPPINGS = {
    "DiscordImageUpload": DiscordImageUpload,
    "DiscordVideoUpload": DiscordVideoUpload,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DiscordImageUpload": "Discord Image Upload",
    "DiscordVideoUpload": "Discord Video Upload",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
