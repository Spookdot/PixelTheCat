import requests
from PIL import Image
from io import BytesIO
from discord.ext import commands


class TagNameConv(commands.Converter):
    async def convert(self, ctx, argument):
        if argument[:3] == "<@!" and argument[-1] == ">":
            usr = await ctx.bot.fetch_user(argument[3:-1])
            return usr.name
        else:
            return argument


class ImageUserConv(commands.Converter):
    async def convert(self, ctx, argument) -> Image.Image:
        if argument[:3] + argument[-1] == "<@!>":
            print("myes")
            usr = await ctx.bot.fetch_user(argument[3:-1])
            im = Image.open(BytesIO(await usr.avatar_url_as(format="png").read()))
            return im.resize((512, 512))
        elif ctx.message.attachments:
            return Image.open(BytesIO(await ctx.message.attachments[0].read()))
        elif argument[:3] + argument[-1] != "<@!>":
            return Image.open(BytesIO(requests.get(argument).content))
        else:
            return Image.NONE
