import discord, os, random
import requests
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')


bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Bot is online')

@bot.command()
async def dog(ctx):
	r = requests.get("https://dog.ceo/api/breeds/image/random")
	res = r.json()
	embed = discord.Embed()
	embed.set_image(url=res['message'])
	await ctx.send(embed=embed)

@bot.command()
async def wyr(ctx):
	r = requests.get("https://api.truthordarebot.xyz/v1/wyr")
	res = r.json()
	await ctx.send(res['question'])

@bot.command()
async def truth(ctx):
	r = requests.get("https://api.truthordarebot.xyz/v1/truth")
	res = r.json()
	await ctx.send(res['question'])
	
bot.run(TOKEN)