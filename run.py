import codecs
import datetime
import discord
import os

from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

load_dotenv()
bot = discord.Bot()

bot.load_extension('cogs.rules')
print('Rules module started...')

bot.load_extension('cogs.change')
print('Banner module started...')

'''bot.load_extension('cogs.emotes')
print('Emotes module started...')'''

@bot.event
async def on_ready():
    print(f'{bot.user} has been activated')

@bot.slash_command(name = 'role_color')
async def color(ctx):
    user = ctx.author
    guild = bot.get_guild(891345145713270854)
    await ctx.respond(f'{user.top_role.color}')
    

bot.run(os.getenv('token'))