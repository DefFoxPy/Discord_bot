import discord
import asyncio
import config
import requests

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='z!', intents=intents)

@bot.event
async def on_ready():
    print('logged on as', bot.user)

@bot.event
async def on_message(message):
    # Primero procese los eventos
    await bot.process_commands(message) 

    # don't respond to command_prefix
    if message[0:2] == 'z!':
        return

    # don't respond to ourselves
    if message.author == bot.user:
        return
    
    if message.content == 'ping':
        await message.channel.send('Pong.')

@bot.command()
async def facts(ctx, number):
    ''' Usando una API para obtener datos curiosos sobre los números '''
    response = requests.get(f'http://numbersapi.com/{number}')
    await ctx.channel.send(response.text)

async def setup():
    print('Setting up...')

async def main():
    await setup()
    await bot.start(config.TOKEN)

asyncio.run(main())