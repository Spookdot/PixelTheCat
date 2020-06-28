from typing import Union

import discord
from discord.ext import commands


class TagNameConv(commands.Converter):
    async def convert(self, ctx, argument):
        if argument[:3] == "<@!" and argument[-1] == ">":
            usr = await ctx.bot.fetch_user(argument[3:-1])
            return usr.name
        else:
            return argument
