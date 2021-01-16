from dotenv import load_dotenv
import os
import discord

load_dotenv()

token = os.getenv("BOT_TOKEN")\


class DiscordClient(discord.Client):
  async def on_ready(self):
    print("Login as")
    print(self.user)
    print("-------")

  async def on_message(self, message):
    # Whenever a user other than bot says "hi"
    if message.author != self.user:
        if message.content == 'hi':
            await message.channel.send('Hello')

client = DiscordClient()
client.run(token)