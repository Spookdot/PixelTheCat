from typing import Union
from cogs.converters import TagNameConv
import aiohttp
import discord
from discord.ext import commands


class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot
        self.client_session = aiohttp.ClientSession()

    async def get_gif(self, kind: str):
        async with self.client_session.get(f"https://rra.ram.moe/i/r?type={kind}") as r:
            res = await r.json()
            return f"https://rra.ram.moe{res['path']}"

    @commands.command(description="Pat youw fwiends", aliases=["pet"])
    async def pat(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"mmm, pwet the {rp_person}\n{await self.get_gif('pat')}")

    @commands.command(description="Give youw fwiends a huggie")
    async def hug(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"Tight hugs fow {rp_person}\n{await self.get_gif('hug')}")

    @commands.command(description="Cuddle wuddle youw fwiends! OwO", aliases=["snuggle"])
    async def cuddle(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"Tight cuddle wuddles fow {rp_person}\n{await self.get_gif('cuddle')}")

    @commands.command(description="The sinnaws shall be slapped ÒwÓ")
    async def slap(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"Giving {rp_person} what they desewve ÒwÓ\n{await self.get_gif('slap')}")

    @commands.command(description="Spwead them Germs")
    async def lick(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"OwO, {ctx.author.name} licked {rp_person}\n{await self.get_gif('lick')}")

    @commands.command(description="Call those sinnaws' sins out ÒwÓ")
    async def lewd(self, ctx, rp_person: TagNameConv = "someone"):
        await ctx.send(f"{rp_person} has sinned!\n{await self.get_gif('lewd')}")

    @commands.command(description="Give chur fwiends a kiss OwO")
    async def kiss(self, ctx, rp_person: TagNameConv):
        await ctx.send(f"Aww, kisees fwom {ctx.author.name} fow {rp_person}\n{await self.get_gif('kiss')}")

    @commands.command(description="Applaud chur fwiends", aliases=["applause", "applaud"])
    async def clap(self, ctx, rp_person: TagNameConv = ""):
        await ctx.send(f"{ctx.author.display_name} put theiw paws togethaw "
                       f"{f'fow {str(rp_person)} ' if rp_person != '' else ''}OwO"
                       f"\n{await self.get_gif('clap')}")

    @commands.command(description="NYA!", aliases=["nyanya"])
    async def nya(self, ctx):
        await ctx.send(f"Nya!\n{await self.get_gif('nyan')}")

    @commands.command(description="OwO")
    async def owo(self, ctx):
        await ctx.send(f"_**OwO**_\n{await self.get_gif('owo')}")

    @commands.command(description="Expwess youw eating")
    async def nom(self, ctx):
        await ctx.send(f"{ctx.author.name} is doing a nom\n{await self.get_gif('nom')}")

    @commands.command(description="Test the API OwO")
    async def do(self, ctx, kind: str, rp_person: TagNameConv = ""):
        if rp_person != "":
            await ctx.send(f"Did a {kind} to {rp_person}\n{await self.get_gif(kind)}")
        else:
            await ctx.send(f"Did a {kind}\n{await self.get_gif(kind)}")
