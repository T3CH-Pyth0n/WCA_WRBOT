import discord
from bs4 import BeautifulSoup as bs
from discord.ext import commands
from urllib import request
client = commands.Bot(command_prefix=".")


def data_ext(event):
    cube_page = request.urlopen(f'https://www.worldcubeassociation.org/results/rankings/{event}/single')
    soup = bs(cube_page, 'html.parser')
    rank_table = soup.find('tbody')
    ranks = rank_table.find_all("tr")[0:]
    positions = []
    names = []
    results = []
    for rank in ranks:
        positions.append(rank.find('td', class_="pos").text)
        names.append(rank.find('td', class_="name").a.text)
        results.append(rank.find('td', class_="result").text)
    return f"{names[0]}: {results[0]}"


@client.event
async def on_ready():
    print("bot is ready")

@client.command(name="2x2")
async def _2(ctx):
    data = data_ext('222')
    await ctx.send(data)

@client.command(name="3x3")
async def _3x3(ctx):
    data = data_ext('333')
    await ctx.send(data)

@client.command(name="4x4")
async def _4(ctx):
    data = data_ext('444')
    await ctx.send(data)

@client.command(name="5x5")
async def _5(ctx):
    data = data_ext('555')
    await ctx.send(data)

@client.command(name="6x6")
async def _6(ctx):
    data = data_ext('666')
    await ctx.send(data)

@client.command(name="7x7")
async def _7(ctx):
    data = data_ext('777')
    await ctx.send(data)

@client.command(name="skewb")
async def _sk(ctx):
    data = data_ext('skewb')
    await ctx.send(data)

@client.command(name="squan")
async def _sq(ctx):
    data = data_ext('sq1')
    await ctx.send(data)

@client.command(name="pyraminx")
async def _pyr(ctx):
    data = data_ext('pyram')
    await ctx.send(data)

@client.command(name="megaminx")
async def _mega(ctx):
    data = data_ext('minx')
    await ctx.send(data)

@client.command(name="3bld")
async def _3bld(ctx):
    data = data_ext('333bf')
    await ctx.send(data)

@client.command(name="4bld")
async def _4bld(ctx):
    data = data_ext('444bf')
    await ctx.send(data)

@client.command(name="5bld")
async def _5bld(ctx):
    data = data_ext('555bf')
    await ctx.send(data)

@client.command(name="mbld")
async def _mbld(ctx):
    data = data_ext('333mbf')
    await ctx.send(data)

@client.command(name="oh")
async def _oh(ctx):
    data = data_ext('333oh')
    await ctx.send(data)

@client.command(name="clock")
async def _clock(ctx):
    data = data_ext('clock')
    await ctx.send(data)

@client.command(name="fmc")
async def _fmc(ctx):
    data = data_ext('333fm')
    await ctx.send(data)


client.run('NzE0MDMxMjkwMDU1MTMxMTM4.XsoviQ.5UbMsd5LKfvsivSyzsb1Ihs4iHY')