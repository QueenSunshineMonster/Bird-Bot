import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    
@client.event
async def on_message(msg):
    if msg.content.startsWith('ping'):
      await client.send_message(msg.channel,   'Pong!')
      
client.run('bot_token')
