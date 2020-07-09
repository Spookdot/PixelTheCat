import textwrap

import requests
from PIL import Image, ImageDraw, ImageFont
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
            usr = await ctx.bot.fetch_user(argument[3:-1])
            im = Image.open(BytesIO(await usr.avatar_url_as(format="png").read()))
            return im.resize((512, 512))
        elif argument[:3] + argument[-1] != "<@!>" and argument != "":
            try:
                return Image.open(BytesIO(requests.get(argument).content))
            except requests.exceptions.MissingSchema:
                impact = BytesIO(
                    requests.get("http://allfont.ru/cache/fonts/impact_830fdfda7ddd8b410acf50522c14d4f9.ttf").content
                )
                cpl, txt = 50, ""
                im = Image.new("RGBA", (1000, 50 * (len(argument) // cpl + 1)), (255, 255, 255, 255))
                font = ImageFont.truetype(font=impact, size=40)
                d = ImageDraw.Draw(im)
                for i in argument.split():
                    if d.textsize(txt[-(txt[::-1].index("\n")) if "\n" in txt else 0:]+i, font=font)[0] < 1000:
                        txt += f"{i} "
                    else:
                        txt += f"\n{i} "
                d.multiline_text((0, 0), txt, font=font, fill=(0, 0, 0, 255))
                if "\n" not in txt:
                    print(d.textsize(txt, font=font)[0])
                    im = im.crop((0, 0, d.textsize(txt, font=font)[0], im.height))
                return im
        else:
            return Image.NONE
