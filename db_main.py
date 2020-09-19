import os
import discord
from discord.ext import commands

db_bot = commands.Bot(command_prefix = '.!')
TOKEN = 'NzU2NjMxMTEwNDQ3OTIzMzQz.X2Upog.1Orq3otQwkxRwYRUeeGVCLsjefg' #os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@db_bot.event
async def on_ready():
    print("Bot Ready!")

@db_bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

db_bot.run(TOKEN)