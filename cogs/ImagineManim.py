import yaml
import discord
from PIL import Image
from io import BytesIO
from discord.ext import commands
from cogs.converters import ImageUserConv


class ImagineManim(commands.Cog, name="ImagineManim"):
    def __init__(self, bot):
        self.bot = bot
        temp_yaml = yaml.load(open("config.yaml", "r"))
        self.meme_pos = temp_yaml["Memes"]

    def make_meme(self, meme: str, user1: Image, user2: Image = None):
        mem = self.meme_pos[meme.lower()]
        img = Image.open(mem["image"]).copy()
        img.paste(user1.resize(mem["user1_resize"]), mem["user1"])
        if user2 is not None:
            img.paste(user2.resize(mem["user2_resize"]), mem["user2"])
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
    async def beautiful(self, ctx, rp_person: ImageUserConv = Image.NONE):
        if rp_person == Image.NONE:
            await ctx.send("OnO, seems chu hav nothing to admiwe")
            return
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        mem = self.meme_pos["beautiful"]
        img = Image.open(mem["image"]).copy()
        img.paste(user1.resize(mem["user1_resize"]), mem["user1"])
        img.paste(user1.resize(mem["user2_resize"]), mem["user2"])
        rp_person.thumbnail((800, 800))
        img.paste(rp_person, ((img.width-rp_person.width)//2, img.height-(450+rp_person.height)))
        img = img.crop((0, img.height-(450+rp_person.height), img.width, img.height))
        file = BytesIO()
        img.save(file, format="PNG")
        file.seek(0)
        await ctx.send(file=discord.File(file, filename="beautiful.png"))
