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

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
	if reason == None:
		reason = "No reason provided"
	await ctx.guild.kick(member)  
	await ctx.send(f'**User: **{member.mention} has been kicked for: *{reason}*')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
	if reason == None:
		reason = "No reason provided"
	await ctx.guild.ban(member)  
	await ctx.send(f'**User: **{member.mention} has been Banned for: *{reason}*')

bot.run(TOKEN)