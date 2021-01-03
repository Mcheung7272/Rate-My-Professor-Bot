# bot.py
import os
from newscrape import searchFull,nss
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='?')
bot.remove_command('help')

@bot.command()
async def search(ctx, *, args):
    parts = searchFull(args)
    if "error" in parts:
        await ctx.channel.send('Error! ' + args + ' not found. Make sure you type the name correctly! If you need help, use ?help {}'.format(ctx.message.author.mention))
    else:
        embedVar = discord.Embed(title="RateMyProfessor Results", description="Professor " + args, color=0x00ff00)
        embedVar.add_field(name="School", value =parts[2], inline=False)
        embedVar.add_field(name="Department", value=parts[0], inline=False)
        embedVar.add_field(name="Class Rating", value=parts[8], inline=False)
        embedVar.add_field(name="Total Reviews", value=parts[7], inline=False)
        embedVar.add_field(name="Overall Rating", value=parts[11], inline=False)
        embedVar.add_field(name="Link", value = "Rate My Professor Link ----> [Click here](https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(parts[6])+ "&showMyProfs=true)", inline=False)
        embedVar.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
        await ctx.channel.send(embed=embedVar)
        await ctx.channel.send("Here you go {}!".format(ctx.message.author.mention))

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def ns(ctx,name):
    results = nss(name.capitalize())
    if("error" in results):
        await ctx.channel.send("No results or incorrect input! If you need help, use !help")
    else:
        embedVar = discord.Embed(title="Search Results for " + name, description = results, color = 0x00ff00)
        await ctx.channel.send(embed=embedVar)

@bot.command()
async def helpme(ctx):
    values = " "
    embedVar = discord.Embed(title="Commands: ", description="Commands and Usage", color=0x00ff00)
    embedVar.add_field(name="?search", value="<First Name> *space* <Last Name>", inline=True)
    embedVar.add_field(name="Use", value="If you know the name of the professor.", inline=True)
    embedVar.add_field(name=chr(173), value=chr(173), inline=False)
    embedVar.add_field(name="?ns", value="<First or Last Name>", inline=True)
    embedVar.add_field(name="Use", value="If you only know the first or last name", inline=True)
    await ctx.channel.send(embed=embedVar)

bot.run(TOKEN)
