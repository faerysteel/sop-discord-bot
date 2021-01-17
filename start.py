from bot.bot import DiscordBot
from bot.giphy import Giphy

gif = Giphy()
bot = DiscordBot(gif)
bot.run()
