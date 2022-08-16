'''
Enviar un mensaje a un canal y borrarlo
'''
import discord
import os
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType #manejo de errores
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
RESPUESTAS_ID = int(os.getenv('CANA_RESPUESTAS_ID'))
CANAL_BIENVENIDA = int(os.getenv('CANAL_BIENVENIDA'))
ROL = int(os.getenv('ROL'))

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Bot is online')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"Comando en cooldown, intenta en: {round(error.retry_after, 2)} segundos", delete_after = 5)

@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(CANAL_BIENVENIDA)
	await channel.send('GoodBye')

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(CANAL_BIENVENIDA)
	await channel.send(f'Saludos {member.mention}')

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def respuesta(ctx, *, mensaje:str):
	# informacion del emisor del mensaje
	member = ctx.author
	name  = member.display_name
	pfp = member.display_avatar
	try:
		await ctx.message.delete()
		for rol in member.roles:
			if rol.id == ROL:
				#creacion del embed con los datos del mensaje
				embed = discord.Embed(
					title='respuesta',
					description = mensaje,
					color = discord.Color.red())
				embed.set_author(name=f'{name}')
				embed.set_thumbnail(url=f'{member.display_avatar}')
				embed.add_field(name='tag', value=member.mention)

				channel = bot.get_channel(RESPUESTAS_ID)
				await channel.send(embed=embed)
				await ctx.send(f'Su respuesta ha sido registrada {member.mention}', delete_after = 5)
				return
		await ctx.send(f'No cuentas con el rol de eventos para participar {member.mention}', delete_after = 5)
	except:
		await ctx.send('No se pudo encontra el canal', delete_after = 5)

bot.run(TOKEN)