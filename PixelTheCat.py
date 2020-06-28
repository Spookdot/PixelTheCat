import toml
from cogs.admin import Admin
from cogs.event import Event
from discord.ext import commands

cfg = toml.load("config.toml")
bot = commands.Bot(command_prefix="!mew ", owner_id="475316891028815873")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")


@bot.command()
async def echo(ctx, *, args):
    await ctx.send(args)


bot.add_cog(Admin(bot))
bot.add_cog(Event(bot))
bot.run(cfg["Bot"]["token"])
