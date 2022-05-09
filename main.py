import discord
from discord.ext import commands
import requests
import json

from aplkeys import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = 't!', intents=intents)


@client.event
async def on_ready():
	print('The bot is now ready for use!')
	print('-----------------------------')	

@client.command()
async def hello(ctx):
	await ctx.send('Hello, I am the bot')	

@client.event
async def on_member_join(member):

    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

	payload = {
	"content": "A joke here",
	"nsfw": "false"
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Host": "joke3.p.rapidapi.com",
		"X-RapidAPI-Key": JOKEAPI
	}

	response = requests.request("POST", jokeurl, json=payload, headers=headers)

	channel = client.get_channel(954536854273794068)
	await channel.send('Welcome, to server')
	await channel.send(json.loads(response.text)['content'])

@client.event
async def on_member_remove(member):
	channel = client.get_channel(954536854273794068)
	await channel.send('GoodBye')


client.run(BOTTOKEN)