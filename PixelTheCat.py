import yaml
import discord
from cogs.fun import Fun
from cogs.event import Event
from cogs.admin import Admin
from cogs.ImagineManim import ImagineManim
from discord.ext import commands

cfg = yaml.load(open("config.yaml", "r"))
bot = commands.Bot(command_prefix="!mew ", owner_id="475316891028815873", case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")


@bot.command()
async def echo(ctx, *, args=""):
    await ctx.send(args)


@bot.command()
async def help(ctx):
    output = discord.Embed(title="Help")
    for i in bot.cogs:
        if "".join([str(j) for j in bot.cogs[i].walk_commands()]) == "":
            continue
        cmnds = "\n".join([f"{', '.join([str(j)] + j.aliases)} - {j.description}" for j in bot.cogs[i].walk_commands()])
        output.add_field(name=i, value=cmnds, inline=False)
    await ctx.send(embed=output)


bot.add_cog(Admin(bot))
bot.add_cog(Fun(bot))
bot.add_cog(Event(bot))
bot.add_cog(ImagineManim(bot))
bot.run(cfg["Bot"]["token"])
