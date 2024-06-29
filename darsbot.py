from db import db
from discord.ext import commands
from discord import Intents, Game, ActivityType, Status, Poll, Embed
from dotenv import load_dotenv
from os import environ
from datetime import timedelta
import requests #remove later!

from help.helpmessage import helpmessage
from act.action import doaction

load_dotenv()

db["month"] = 1

bot_token = environ["bot_token"]

intents = Intents.default()
intents.message_content = True
intents.presences = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

"""
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        embed = Embed(title = f"Command not found",
                      description = "Make sure you've spelled everything right!",
                      color = 0xff0000)
        await ctx.reply(embed = embed)
        return
"""

@bot.event
async def on_ready():
  botactivity = Game(name="Vartok Multinational Survey", type=ActivityType.playing,)
  await bot.change_presence(activity=botactivity, status=Status.online)

  print(f'Logged in as {bot.user.name}')

@bot.command()
async def apples(ctx):
    await ctx.reply("yay!")

@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 696811705619054633:
        await ctx.reply('Shutting down...')
        await bot.close()
    else:
        await ctx.reply("You don't have permission to shut down the bot.")

@bot.command()
async def help(ctx, command = "default"):
    await ctx.reply(embed = helpmessage(command))

@bot.command()
async def act(ctx, command = None):
    await ctx.reply(embed = doaction(command, str(ctx.message.author.id)))

@bot.command()
async def rule(ctx, *, rule):
    ruleschannel = bot.get_channel(1254996321694384210)
    rulesvote = Poll(rule, timedelta(hours = 2)).add_answer(text = "yay!", emoji = "✅").add_answer(text = "no :(", emoji = "❌")
    await ruleschannel.send(poll = rulesvote)

@bot.command(aliases=[":3"])
async def imageofacat(ctx):
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  data = response.json()
  image_url = data[0]['url']
  embed =  Embed(title="", color=0xFFA500)
  embed.set_image(url=image_url)

  await ctx.reply(embed=embed)

@bot.command(aliases=["vdb"])
async def viewdb(ctx):
    for i in db.keys():
        print(f"{i}: {db[i]}")

bot.run(bot_token)
