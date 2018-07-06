import discord
from discord.ext import commands
import random

token = "YOUR TOKEN"

description = '''like thomleg except more intelligent'''
bot = commands.Bot(command_prefix='t', description=description)
thomone = ["can ",
                "can to ",
                "you can ",
                "any here ",
                "any here can ",
                "any here can to ",
                "can you "]
thomtwo = ["pls help ",
                "pls help to ",
                "pls to help with ",
                "please help with ",
                "please help to ",
                "respond to me ",
                "respond to me about ",
                "respond about ",
                "how to ",
                "how to do ",
                "reply me pls ",
                "reply pls about ",
                "help me with "]
thomannoying = ["build atmosphere ",
                "make atmosphere ",
                "build atmos ",
                "make atmos ",
                "hactool ",
                "version bot ",
                "versionlist ",
                "setup bot ",
                "webhook "]
thomthree = ["please ",
                "i dont understand ",
                "then do "]
thomerunningoutofnames = ["?",
                "!",
                "..."]


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='homleg')
async def homleg():
    """Gives you a thomleg question"""
    await bot.say(random.choice(thomone) + random.choice(thomtwo) + random.choice(thomannoying) + random.choice(thomthree) + random.choice(thomerunningoutofnames))

bot.run(token)
