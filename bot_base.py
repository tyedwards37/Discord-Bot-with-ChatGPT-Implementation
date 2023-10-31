# @file bot.py
# @brief - This is a base code for setting up a Discord bot that reall respond to being mentioned (@ function).
# @author Tyler Edwards - tk.edwards2003@gmail.com

import discord
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # getting tokens from .env
#TOKEN = '[TOKEN]'

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if client.user.mentioned_in(message):
        await message.channel.send('Hey there, pal!')

client.run('[TOKEN]')