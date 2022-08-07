import discord, os, random
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
	await ctx.reply(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball', 'test']) # se puede agregar alias al comando
async def eightball(ctx, *, question):  # permite que el parametro tenga muchos espacios
	responses = ['yes', 'no', 'maybe']
	await ctx.send(f'**Question: **{question}\n**Answers: **{random.choice(responses)}')



bot.run(TOKEN)