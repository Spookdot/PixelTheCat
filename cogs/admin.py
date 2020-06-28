from discord.ext import commands
from discord.ext.commands import command, has_guild_permissions, bot_has_guild_permissions


class Admin(commands.Cog, name="Admin"):
    def __init__(self, bot):
        self.bot = bot

    @command(desc="cleans this place of youw filth")
    @has_guild_permissions(manage_messages=True)
    @bot_has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, arg1: int):
        n = await ctx.channel.purge(limit=arg1)
        await ctx.send(f"Puwged {len(n)} of youw filth UwU")
