import discord
from discord.ext import commands
import random

token = "YOUR TOKEN"

description = '''Simulates stupid questions'''
bot = commands.Bot(command_prefix='t', description=description)
one = ["can ",
                "can to ",
                "you can ",
                "any here ",
                "any here can ",
                "any here can to ",
                "can you "]
two = ["pls help ",
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
annoying = ["build atmosphere ",
                "make atmosphere ",
                "build atmos ",
                "make atmos ",
                "hactool ",
                "version bot ",
                "versionlist ",
                "setup bot ",
                "webhook "]
three = ["please ",
                "i dont understand ",
                "then do "]
runningoutofnames = ["?",
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
    """Gives you a stupid question"""
    await bot.say(random.choice(one) + random.choice(two) + random.choice(annoying) + random.choice(three) + random.choice(runningoutofnames))

bot.run(token)
