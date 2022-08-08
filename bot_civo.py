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
async def embed(ctx, member:discord.Member = None):
	if member == None:
		member = ctx.author

	name = member.display_name
	pfp = member.display_avatar

	embed = discord.Embed(title="This is my embed", description='Its a very cool embed', color = discord.Colour.random())
	embed.set_author(name=f'{name}', url='https://cdn-icons-png.flaticon.com/512/2/2181.png', icon_url='https://cdn-icons-png.flaticon.com/512/2/2181.png')
	embed.set_thumbnail(url=f'{pfp}')  
	embed.add_field(name='This is 1 field', value='this field is just value')
	embed.add_field(name='This is 2 field', value='this field is inline true', inline=True)
	embed.add_field(name='This is 3 field', value='this field is inline false', inline=False)
	embed.set_footer(text=f'{name} Made this embed')

	await ctx.send(embed=embed)

bot.run(TOKEN)