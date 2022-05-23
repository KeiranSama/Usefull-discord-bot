import discord
from discord.ext import commands



class Komutlar(commands.cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def oc(self, ctx):
        await ctx.send(f"ORRRRRROSPU ÇOCUĞUUUUUU {ctx}")


def setup(bot):
    bot.add_cog(Komutlar(bot))