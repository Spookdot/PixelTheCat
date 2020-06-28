from discord.ext import commands
from discord import embeds


class Event(commands.Cog, name="Event"):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send("Oopsy! You awen't allowed to do dat!")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send("I can't do that (´・ω・`)")
        elif isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == "rp_person":
                return await ctx.send(f"Vewy sad (´・ω・`) Chu don't have anyone to {ctx.command.name}!")
            else:
                return await ctx.send("Oh nu (´・ω・`) Chu mwissed an awgument!")
        else:
            return await ctx.send("Opsie Wopsie, Chu bwoke the command machine (´・ω・`)",
                                  embed=embeds.Embed(description=str(error)))
