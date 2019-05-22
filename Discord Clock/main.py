import discord
import asyncio
import datetime

client = discord.Client()

distoken = "Your Discord Token"

# These must all be Voice Channels
timechannel = # The ID of the Channel that gets renamed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        now = datetime.datetime.now()
        await client.get_channel(timechannel).edit(name=f"{now.hour}:{now.minute} (<INSERT YOUR LOCAL TIMEZONE HERE>)") # The channel gets changed here
        await asyncio.sleep(60)


client.run(distoken)
