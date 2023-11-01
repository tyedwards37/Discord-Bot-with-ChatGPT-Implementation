# @file bot_with_ai_base.py
# @brief - This is the template for setting up the bot with a given personality and context.
# @author Tyler Edwards - tk.edwards2003@gmail.com

import openai
import discord
import os

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') # getting tokens from .env
#TOKEN = '[TOKEN]'
openai.api_key = os.getenv('OPENAI_TOKEN') # getting tokens from .env
#openai.api_key = '[OPENAI_KEY]'

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

replies = []

personality = "[PERSONALITY]" 
replies.append({"role": "system", "content": personality})
context = "[CONTEXT]" 
replies.append({"role": "system", "content": context})

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if client.user.mentioned_in(message):
        message_content = message.content
        message_author_name = message.author.name

        replies.append({"role": "system", "content": f"{message_author_name}: {message_content}"})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=replies)
        bot_response = message.author.mention + " " + response["choices"][0]["message"]["content"] # NEW - @'S THE PERSON WHO MESSAGED
        replies.append({"role": "system", "content": response["choices"][0]["message"]["content"]})
        await message.channel.send(bot_response)

client.run(TOKEN)
