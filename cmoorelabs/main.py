import discord
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('logged on as', client.user)

@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return
    
    if message.content == 'ping':
        await message.channel.send('Pong.')

async def setup():
    print('Setting up...')

async def main():
    await setup()
    await client.start(config.TOKEN)

asyncio.run(main())