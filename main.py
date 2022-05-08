import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 't!')

@client.event
async def on_ready():
	print('The bot is now ready for use!')
	print('-----------------------------')	

@client.command()
async def hello(ctx):
	await ctx.send('Hello, I am the bot')

client.run('OTcyODcwMjExMjUyMzk2MDYy.GCo8Tl.VYrbLj25cYz8N_rm6NpVm32DxFOflLvoPkCQRw')