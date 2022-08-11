import discord, os, random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all())

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Discord.py"))
	print('Bot is online')

bot.run(TOKEN)