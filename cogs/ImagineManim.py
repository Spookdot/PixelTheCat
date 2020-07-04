import yaml
import discord
import requests
from PIL import Image
from io import BytesIO
from typing import Union
from discord.ext import commands


class ImagineManim(commands.Cog, name="ImagineManim"):
    def __init__(self, bot):
        self.bot = bot
        temp_yaml = yaml.load(open("config.yaml", "r"))
        self.meme_pos = temp_yaml["Memes"]

    def make_meme(self, meme: str, user1: Image, user2: Image = None, user3: Image = None):
        mem = self.meme_pos[meme.lower()]
        img = Image.open(mem["image"]).copy()
        img.paste(user1.resize(mem["user1_resize"]), mem["user1"])
        if user2 is not None:
            img.paste(user2.resize(mem["user2_resize"]), mem["user2"])
        if user3 is not None:
            img.paste(user3.resize(mem["user3_resize"]), mem["user3"])
        file = BytesIO()
        img.save(file, format="PNG")
        file.seek(0)
        return discord.File(file, filename=f"{meme}.png")

    @commands.command(description="Appwoach chur enemy to beat the shit out of them ÒwÓ")
    async def approach(self, ctx, rp_person: discord.User):
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        user2 = Image.open(BytesIO(await rp_person.avatar_url_as(format="png").read()))
        await ctx.send(file=self.make_meme("approach", user1, user2))

    @commands.command(description="Admiwe the bweauty of this pic or purrson")
    async def beautiful(self, ctx, rp_person: Union[discord.User, str] = None):
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        mem = self.meme_pos["beautiful"]
        img = Image.open(mem["image"]).copy()
        img.paste(user1.resize(mem["user1_resize"]), mem["user1"])
        img.paste(user1.resize(mem["user2_resize"]), mem["user2"])
        if isinstance(rp_person, discord.User):
            user2 = Image.open(BytesIO(await rp_person.avatar_url_as(format="png").read()))
            user2 = user2.resize(mem["user3_resize"])
        elif isinstance(rp_person, str):
            user2 = Image.open(BytesIO(requests.get(rp_person).content))
        elif ctx.message.attachments:
            user2 = Image.open(BytesIO(await ctx.message.attachments[0].read()))
        else:
            await ctx.send("OnO, seems chu hav nowing to admiwe")
            return
        user2.thumbnail((800, 800))
        img.paste(user2, ((img.width-user2.width)//2, img.height-(450+user2.height)))
        img = img.crop((0, img.height-(450+user2.height), img.width, img.height))
        file = BytesIO()
        img.save(file, format="PNG")
        file.seek(0)
        await ctx.send(file=discord.File(file, filename="beautiful.png"))
