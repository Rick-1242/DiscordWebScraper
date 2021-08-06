import discord
import logging
import os

from keep_alive import keep_alive

# Setup logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Code
client = discord.Client()


@client.event
async def on_ready():
    print("Ready user {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith("-"):
        await message.channel.send("hello world")


keep_alive()
client.run(os.environ['TOKEN'])
