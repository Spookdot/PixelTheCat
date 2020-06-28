import discord
from discord.ext import commands
from discord.ext.commands import command, has_guild_permissions, bot_has_guild_permissions


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @command(description="cleans this place of youw filth")
    @has_guild_permissions(manage_messages=True)
    @bot_has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, arg1: int):
        n = await ctx.channel.purge(limit=arg1)
        await ctx.send(f"Puwged {len(n)} of youw filth UwU")

    @command(description="Ban the filwy sinners")
    @has_guild_permissions(ban_members=True)
    @bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *, reason=""):
        await ctx.guild.ban(user, reason=reason)
        await ctx.send("Banned the filth OwO")

    @command(description="Kick the filwy sinners")
    @has_guild_permissions(kick_members=True)
    @bot_has_guild_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User, *, reason=""):
        await ctx.guild.kick(user, reason=reason)
        await ctx.send("Kicked the filth OwO")
