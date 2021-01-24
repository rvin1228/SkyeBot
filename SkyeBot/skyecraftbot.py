import discord
import os
from discord.ext import commands

TOKEN = '' #Insert token here

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('skye-craft.com'))
	print('SkyeBot is online.')

#Ping
@client.command(aliases=['ms','net'])
async def ping(ctx):
	await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


@client.command()
async def displayembed(ctx):
	embed = discord.Embed(
		title = 'Title',
		description = 'A skyblock server',
		colour = discord.Colour.orange()

	)

	embed.set_footer(text='This is a footer.')
	embed.set_image(url='https://cdn.discordapp.com/attachments/705354889139716128/722713982347116644/unknown.png')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/705354889139716128/720557309037772950/unknown.png')
	embed.set_author(name='rvin1228', icon_url='https://cdn.discordapp.com/attachments/705354889139716128/720557309037772950/unknown.png')
	embed.add_field(name='Field Name', value='Field Value', inline=False)
	embed.add_field(name='Field Name', value='Field Value', inline=True)
	embed.add_field(name='Field Name', value='Field Value', inline=True)

	await ctx.send(embed=embed)

















@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
