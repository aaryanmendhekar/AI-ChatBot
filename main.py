# app id: 1126033907226267819
# public key: 41c4df877b2b7cb3b794aa2fc451d1e8f9c6693c613be2ed6d9700e508db0616
import discord
import os
import openai


with open("chat.txt", "r") as f:
  chat = f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client): 
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
            if self.user in message.mentions:
              channel = message.channel
              response = openai.Completion.create(
                model="text-davinci-003",
                prompt = f"{chat}\nChatGPT: ",
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
              )
              messageToSend = response.choices[0].text
              await channel.send(messageToSend)



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)