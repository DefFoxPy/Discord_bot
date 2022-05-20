import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json

from aplkeys import *

MUSIC_NAME = 'Rick Astley.mp3'

intents = discord.Intents.default()
intents.members = True

queues = {} 

def check_queue(ctx, id):
	if queues[id] != []:
		voice = ctx.guild.voice_client
		source = queues[id].pop(0)
		player = voice.play(source)

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
		source = FFmpegPCMAudio(MUSIC_NAME)
		player = voice.play(source)
	else:
		await ctx.send('No estas en un canal de voz, debes estar en uno para usar este comando')
'''
@client.command(pass_context = True)
async def rick(ctx, channel : str):
	try:	
		channel = client.get_channel(int(channel))
		voice = await channel.connect()
		source = FFmpegPCMAudio(MUSIC_NAME)
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

@client.command(pass_context = True)
async def pause(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		await ctx.send('En este momento no se está reproduciendo ninguna música.')

@client.command(pass_context = True)
async def resume(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send('En este momento, ninguna música está pausada.')

@client.command(pass_context = True)
async def stop(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	voice.stop()

@client.command(pass_context = True)
async def play(ctx, *, music=MUSIC_NAME):
	voice = ctx.guild.voice_client
	source = FFmpegPCMAudio(music)
	player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

@client.command(pass_context = True)
async def queue(ctx, *, music):
	voice = ctx.guild.voice_client
	source = FFmpegPCMAudio(music)
	guild_id = ctx.message.guild.id

	if guild_id in queues:
		queues[guild_id].append(source)

	else:
		queues[guild_id] = [source]

	await ctx.send("Añadido para la lista de música")



client.run(BOTTOKEN)	