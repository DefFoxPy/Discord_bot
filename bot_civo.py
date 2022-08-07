import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Bot is online')

@bot.command()
async def ping(ctx):
	await ctx.reply('Pong')


bot.run(TOKEN)