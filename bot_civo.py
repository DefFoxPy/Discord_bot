import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Bot is online')

@bot.event
async def on_message(message):
	if message.content.lower() == 'hello':
		await message.channel.send('Hey!')

@bot.event
async def on_member_join(member):
	channel = member.guild.system_channel
	await channel.send(f'{member.mention} Welcomen to the Server.')

@bot.event
async def on_member_remove(member):
	channel = member.guild.system_channel
	await channel.send(f'Goodbye {member.mention}')

@bot.command()
async def ping(ctx):
	await ctx.reply('Pong')


bot.run(TOKEN)