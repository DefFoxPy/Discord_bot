import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
	print('Bot is online')

@bot.group(name="help", invoke_without_command=True) #impide que se vuelva a llamar help en otro comando del grupo
async def help(ctx):
	await ctx.send('Games\nUtilitys\nEcosystem')

@help.command()
async def game(ctx):
	await ctx.send("These are the game comands 'rps'")

@help.command()
async def utilitys(ctx):
	await ctx.send("These are the utilitys comands")

@help.command()
async def eco(ctx):
	await ctx.send("These are the eco comands")


bot.run(TOKEN)