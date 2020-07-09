import yaml
import discord
from PIL import Image, ImageChops
from io import BytesIO
from discord.ext import commands
from cogs.converters import ImageUserConv


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


class ImagineManim(commands.Cog, name="ImagineManim"):
    def __init__(self, bot):
        self.bot = bot
        temp_yaml = yaml.safe_load(open("config.yaml", "r"))
        self.meme_pos = temp_yaml["Memes"]

    def make_meme(self, meme: str, *users):
        mem = self.meme_pos[meme.lower()]
        img = Image.open(mem["image"]).copy()
        for i, user in enumerate(users, 1):
            ubox, align = mem[f"user{i}_box"], mem[f"user{i}_align"].split("-")
            user.thumbnail([ubox[j+2] - ubox[j] for j in range(2)])
            box = [
                ubox[0] if align[1] == "left" else
                (ubox[2] - ubox[0] - user.width) // 2 + ubox[0] if align[1] == "center" else
                ubox[2] - user.width if align[1] == "right" else 0,
                ubox[1] if align[0] == "upper" else
                (ubox[3] - ubox[1] - user.height) // 2 + ubox[1] if align[0] == "center" else
                ubox[3] - user.height if align[0] == "lower" else 0
            ]
            img.paste(user, box)
        img = trim(img)
        file = BytesIO()
        img.save(file, format="PNG")
        file.seek(0)
        return discord.File(file, filename=f"{meme}.png")

    @commands.command(description="Appwoach chur enemy to beat the shit out of them ÒwÓ")
    async def approach(self, ctx, *, rp_person: ImageUserConv = Image.NONE):
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        user2 = Image.open(BytesIO(await ctx.message.attachments[0].read())) if ctx.message.attachments else rp_person
        assert not rp_person == Image.NONE or ctx.message.attachments, "appwoach"
        await ctx.send(file=self.make_meme("approach", user1, user2))

    @commands.command(description="Admiwe the bweauty of this pic or purrson")
    async def beautiful(self, ctx, *, rp_person: ImageUserConv = Image.NONE):
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        user2 = Image.open(BytesIO(await ctx.message.attachments[0].read())) if ctx.message.attachments else rp_person
        assert not rp_person == Image.NONE or ctx.message.attachments, "admiwe"
        await ctx.send(file=self.make_meme("beautiful", user1, user1, user2))

    @commands.command(description="Place chur twump cawd")
    async def trump(self, ctx, rp_person: ImageUserConv = Image.NONE):
        user1 = Image.open(BytesIO(await ctx.author.avatar_url_as(format="png").read()))
        user2 = Image.open(BytesIO(await ctx.message.attachments[0].read())) if ctx.message.attachments else rp_person
        if not rp_person == Image.NONE or ctx.message.attachments:
            await ctx.send(file=self.make_meme("trump", user1, user2))
        else:
            await ctx.send(file=self.make_meme("trump", user1))
