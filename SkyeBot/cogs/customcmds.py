import discord
import os
from discord.ext import commands

class customCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Custom Commands
    @commands.command()
    async def clear(self, ctx, amount=5):
    	await ctx.channel.purge(limit=amount)
    	await ctx.send("**Removed messages ^_^**")

    @commands.command()
    async def usage(self, ctx):
    	await ctx.send('```ml\n===Usage Commands===\n\nCustom\nping - "Check your current ping."\nclear - "Remove messages (Default: 5)."\n\nModeration\nkick - "Kick a discord user."\nban - "Ban a discord user."\nunban - "Unban a discord user."\n\nAdmin\nload - "Load extensions."\nunload - "Unload extensions."\nreload - "Reload extensions."```')

def setup(client):
    client.add_cog(customCmds(client))
