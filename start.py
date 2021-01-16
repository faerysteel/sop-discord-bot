from dotenv import load_dotenv
import os
from bot import bot

load_dotenv()
token = os.getenv("BOT_TOKEN")

client = bot.DiscordClient()
client.run(token)