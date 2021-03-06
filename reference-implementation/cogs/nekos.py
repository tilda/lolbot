"""
The MIT License (MIT)

Copyright (c) 2018 tilda

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
# noinspection PyPackageRequirements
import discord
import json

# noinspection PyPackageRequirements
from discord.ext import commands

# noinspection PyPackageRequirements
import utils.errors
from cogs.utils.plainreq import get_req
from cogs.utils.endpoints import nekos


class Animemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = json.load(open("config.json"))

    @commands.command()
    async def neko(self, ctx):
        """Shows a neko"""
        async with get_req(ctx.bot.session, nekos["sfw"]) as neko:
            if neko.status == 200:
                img = await neko.json()
                neko_em = discord.Embed(colour=0x690E8)
                neko_em.set_image(url=img["neko"])
                neko_em.set_footer(text="source: nekos.life")
                await ctx.send(embed=neko_em)
            else:
                raise utils.errors.ServiceError(f"non-200: {neko.status})")


def setup(bot):
    bot.add_cog(Animemes(bot))
