import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import discord
except ImportError:
    install("discord.py")

try:
    import nest_asyncio
except ImportError:
    install("nest_asyncio")