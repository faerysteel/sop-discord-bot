from dotenv import load_dotenv
import os
import pprint

import random
from discord.ext.commands import Bot

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_BOT_PREFIX = os.getenv("DISCORD_BOT_PREFIX")


class DiscordBot:
    def __init__(self, gif):
        self.gif = gif
        self.bot = Bot(command_prefix=DISCORD_BOT_PREFIX)

    def run(self):
      bot = self.bot

      @bot.event
      async def on_ready():
          print("Login as")
          print(bot.user.name)
          print("-------")


      @bot.command(name='8ball')
      async def magic_eight_ball(ctx):
          response = [
              'Without a doubt.',
              'Outlook good.',
              'Better not tell you now.',
              'Cannot predict now.',
              'My reply is no.',
              'Outlook not so good.',
          ]
          await ctx.send(random.choice(response))

      @bot.command(name='rgif', description="Post a random gif")
      async def send_random_gif(ctx):
        await ctx.send(self.gif.get_random())

      @bot.command(name='tgif', description="Post a random gif from the top trending gifs")
      async def send_trending_gif(ctx):
        await ctx.send(self.gif.get_trending())

      @bot.command(name='gif', description=f"Search for and post a random gif from the top results")
      async def send_gif(ctx, *, arg=None):
        if arg is None:
          await ctx.invoke(bot.get_command('rgif'))
        else:
          await ctx.send(self.gif.get_search(arg))

      bot.run(DISCORD_BOT_TOKEN)
