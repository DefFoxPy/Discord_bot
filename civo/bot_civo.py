import discord, os
from datetime import datetime
import sqlite3
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

bot = commands.Bot(command_prefix='z/', intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
	db = sqlite3.connect("warning.sqlite")
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS warns(user INTERGER, reason TEXT, time INTERGER, guild INTERGER)")
	print('Bot is online')

async def addawarn(ctx, reason, user):
	db = sqlite3.connect("warning.sqlite")
	cursor = db.cursor()
	cursor.execute("INSERT INTO warns (user, reason, time, guild) VALUES (?, ?, ?, ?)", [user.id, reason, int(datetime.now().timestamp()), ctx.guild.id])
	db.commit()

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member:discord.Member, *, reason:str = "No reason"):
	await addawarn(ctx, reason, member)
	await ctx.send(f"Warned {member.mention} for {reason}")

	db = sqlite3.connect("warning.sqlite")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM warns WHERE user = ? AND guild = ?", [member.id, ctx.guild.id])
	data = cursor.fetchall()
	if len(data) >= 3:
		muteRole = discord.utils.get(ctx.guild.roles, name='Muted')
		await member.add_roles(muteRole)
		await ctx.send("You have been warned {len(data)} times and your are now temp muted")
		await asyncio.sleep(60)
		await member.remove_roles(muteRole)
		await ctx.send(f"{member.mention} you have been unmuted")

@bot.command()
async def removewarn(ctx, member:discord.Member):
	db = sqlite3.connect("warning.sqlite")
	cursor = db.cursor()
	cursor.execute("SELECT reason FROM warns WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
	data = cursor.fetchone()
	if data:
		cursor.execute("DELETE FROM warns WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
		await ctx.send('Warns have been removed.')
	else:
		await ctx.send('You dont have any warnings')
	db.commit()	

bot.run(TOKEN)

