import discord
from discord.ext import commands
from utils import *
from functions import *
import random
import requests

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!", intents=intents)
game = Game()


@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="GELİŞTİRİLİYOR"))
    print("Ben Hazırım")


@Bot.event
async def on_member_Join(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş")
    await channel.send(f"{member} Aramıza Katıldı. Hoşgeldin {member}")
    print(f"{member} Aramıza Katıldı. Hoşgeldin {member}")


async def on_member_Join(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş")
    await channel.send(f"{member} Aramızdan Ayrıldı. Siktir  Git :)))){member}")
    print(f"{member} gitti siktir git {member}")


@Bot.command()
async def dayi(ctx, ):
    await ctx.send("**DAYICIIIIIIM**")


@Bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@Bot.command()
async def oc(ctx):
    await ctx.send("**SEN BİR ORROSPU ÇOCUĞUSUN :))**")


@Bot.command()
async def zar(ctx):
    print(ctx.message)
    if ctx.author.name == "Beşinci Hugo":
        await ctx.send(f"**{ctx.author.name},"  f" attğın zar {r(0, 75)}**")
    elif ctx.author.name == "Emre Can":
        await ctx.send(f"**{ctx.author.name},"  f" attğın zar {r(25, 100)}**")
    elif ctx.author.name == "scoasmaca/METO":
        await ctx.send(f"**{ctx.author.name},"  f" attğın zar {r(0, 100)}**")
    else:
        await ctx.send(f"**{ctx.author.name},"  f" attğın zar {r(0, 100)}**")


@Bot.command()
async def sa(ctx):
    await ctx.send(f"**{ctx.author.name} Aleyküm Selam Sevgili Kardeşim**")
    await ctx.send("**Nasılsın İyisin İnşallah**")


@Bot.command()
async def iyiyim(ctx):
    await ctx.send(f"**{ctx.author.name} Ne Güzel Senin Adına Sevindim**")


@Bot.command()
async def kötüyüm(ctx):
    await ctx.send(f"**{ctx.author.name} Olur öyle arada kardeşim bu günlerde geçer** ")


@Bot.command()
async def benkacar(ctx):
    await ctx.send("**HADİ SEKTİRRRRR GİT AMINA KOYM**")


@Bot.command()
async def nereye(ctx):
    rastgele = random.choice(sehirler)
    await ctx.send(
        f"**Bugün Buraya Gitsek Çok İyi Olur  {rastgele}**\n**Al Sana Link Gez Dolaş**\nhttps://www.google.com/maps/place/{rastgele}")


@Bot.command()
async def film(ctx, *args):
    degisken=args
    response = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key=b0e5307218c0a485a55da9c5ceb150f6&query={degisken}")
    response.text
    response.headers.get("Content-Type")
    response.json()
    results = response.json()["results"]
    i = 0
    try:
        while True:
            if i == 5:
                break
            await ctx.send(f"{i + 1}. Önerimiz: " + results[i]["original_title"])
            i += 1
    except:
        await ctx.send(f"{degisken} Bulunamadı")

Bot.run(TOKEN)
