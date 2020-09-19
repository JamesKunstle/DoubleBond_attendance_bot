import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from typing import List

client = commands.Bot(command_prefix = '.!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    print("Bot Ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Current latency: {round( client.latency * 1000) }ms ')

@client.command()
async def attendance(ctx, *, inputs):
    input_tokens: List = inputs.split(" ")
    for token in input_tokens:
        await ctx.send(f'token read: {token}')

@client.command()
async def kick_restricted(ctx, member: discord.Member, *, kick_reason=None):
    await member.kick(reason=kick_reason)

client.run(TOKEN)