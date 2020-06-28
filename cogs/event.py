from discord.ext import commands
from discord import embeds


class Event(commands.Cog, name="Event"):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send("Oopsy! You awen't allowed to do dat!")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send("I can't do that (´・ω・`)")
        else:
            return await ctx.send("Opsie Wopsie, I don't know what happen' either (´・ω・`)",
                                  embed=embeds.Embed(description=str(error)))
