# @file ai_base.py
# @brief - This is the base code for setting up a responsive ChatGPT instance. 
# @author Tyler Edwards - tk.edwards2003@gmail.com

import openai
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_TOKEN') # getting tokens from .env
#openai.api_key = "[KEY]"

replies = []

personality = "[CHARACTER]" 
replies.append({"role": "system", "content": personality})
context = "[CONTEXT]" 
replies.append({"role": "system", "content": context})

user_response = input("Say hello to [CHARACTER]! \n")
replies.append({"role": "system", "content": user_response})

print("\nIf they ever get annoying, tell them to \"Shut up!\"")
while user_response != "Shut up!":
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=replies)
    bot_response = response["choices"][0]["message"]["content"]
    replies.append({"role": "system", "content": bot_response})
    print("\n" + bot_response + "\n")

    user_response = input()
    replies.append({"role": "system", "content": user_response})

