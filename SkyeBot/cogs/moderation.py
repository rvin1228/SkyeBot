import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Events
    #@commands.Cog.listener()
    #async def on_ready(self):
        #print('SkyeBot is online.')

    #Kick, Ban, and Unban Functions
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
    	await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
    	await member.ban(reason=reason)
    	await ctx.send(f'Banned {member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):
    	banned_users = await ctx.guild.bans()
    	member_name, member_discriminator = member.split('#')

    	for ban_entry in banned_users:
    		user = ban_entry.user

    		if(user.name, user.discriminator) == (member_name, member_discriminator):
    			await ctx.guild.unban(user)
    			await ctx.send(f'Unbanned {user.mention}')
    			return


def setup(client):
    client.add_cog(Moderation(client))
