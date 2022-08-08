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
	print('Bot is online')

class MyBot(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.default())
		self.synced = False

	async def on_ready(self):
		await tree.sync(guild=discord.Object(id=SERVER_ID))
		self.synced = True
		print('Bot is online')

bot = MyBot()
tree = app_commands.CommandTree(bot)

@tree.command(name='ping', description='Pings the user', guild=discord.Object(id=SERVER_ID))
async def self(interaction:discord.Interaction):
	await interaction.response.send_message(f'Pong')

@tree.command(name='eightball', description='gives your a answer', guild=discord.Object(id=SERVER_ID))
async def self(interaction:discord.Interaction, question:str):
	responses = ['yes', 'no', 'maybe']
	await interaction.response.send_message(f'**Question: **{question}\n**Answers: **{random.choice(responses)}')	

bot.run(TOKEN)