import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
