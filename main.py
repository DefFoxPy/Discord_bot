import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json

from aplkeys import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = 'w!', intents=intents)


@client.event
async def on_ready():
	print('The bot is now ready for use!')
	print('-----------------------------')	

@client.command()
async def hello(ctx):
	await ctx.send('Hello, I am the bot')	

@client.event
async def on_member_join(member):

	await channel.send('Welcome, to server')
	
@client.event
async def on_member_remove(member):
	channel = client.get_channel(954536854273794068)
	await channel.send('GoodBye')

@client.command(pass_context = True)
async def join(ctx):
	if (ctx.author.voice):
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
		source = FFmpegPCMAudio('Rick Astley.mp3')
		player = voice.play(source)
	else:
		await ctx.send('No estas en un canal de voz, debes estar en uno para usar este comando')
'''
@client.command(pass_context = True)
async def rick(ctx, channel : str):
	try:	
		channel = client.get_channel(int(channel))
		voice = await channel.connect()
		source = FFmpegPCMAudio('Rick Astley.mp3')
		player = voice.play(source)
	except ValueError:
		await ctx.send('la id no es un número entero')
	except AttributeError:
		await ctx.send('la id es invalida')
'''

@client.command(pass_context = True)
async def leave(ctx):
	if (ctx.voice_client):
		await ctx.guild.voice_client.disconnect() 
	else:
		await ctx.send('No estoy en ningún canal de voz')

client.run(BOTTOKEN)	