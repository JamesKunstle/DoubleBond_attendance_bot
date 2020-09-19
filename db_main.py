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
async def DotBang(ctx, input_section=None):
    if input_section == "-help":
        await ctx.send(f"__Available bot services__")
        await ctx.send(f"ping")
        await ctx.send(f"attendance <-p> <-s> <Voice_Channel_Name>")
        await ctx.send(f"list_channels")
        await ctx.send(f"list_channel_members <Voice_Channel_Name>")
    else:
        await ctx.send(f"DotBang is a bot written by James Kunstle.")
        await ctx.send(f"It supports some basic functionalities at the moment with more on the way.")
        await ctx.send(f"WARNING: Failures are not verbose. If there is no output then a command has failed.")
        await ctx.send(f"Please enter: \".!DotBang -help\" for more information.""")

@client.command()
async def attendance(ctx, *, inputs):

    # -p = print to screen
    # -s = save absent to buffer

    input_tokens: List = inputs.split(" ")
    p_flag: bool = False
    s_flag: bool = False

    
    if "-p" in input_tokens:
        p_flag = True

    if "-s" in input_tokens:
        s_flag = True

    channel_name: str = "" #this is how we access the channel that we are taking attendance in.

    for token in input_tokens:
        if token[0] == "\"" :
            channel_name += (token[1:] + " ")
        elif token[-1] == "\"":
            channel_name += token[:-1]


    #This is the beginning of handling channel details.

    channels: List = client.guilds[0].voice_channels

    current_channel: discord.VoiceChannel = None

    for channel in channels:
        if str(channel) == channel_name:
            current_channel = channel
    
    those_in_channel = [mem.nick for mem in current_channel.members]
    those_total = [mem.nick for mem in client.guilds[0].members]

    those_absent = set(those_total) - (set(those_in_channel) & set(those_total))

    if p_flag:
        if len(those_absent) > 0:
            await ctx.send(f"____Those that were absent____")

            for absent in those_absent:
                await ctx.send(f"~~{absent}")

            await ctx.send(f"____Those that were present____")

            for present in set(those_in_channel):
                await ctx.send(f"~~{present}")

        await ctx.send("--Attendance Complete--")
    
    if s_flag:
        await ctx.send(f"/saving not currently supported/")


@client.command()
async def kick_restricted(ctx, member: discord.Member, *, kick_reason=None):
    await member.kick(reason=kick_reason)

@client.command()
async def list_channels(ctx):
    channels: List = client.guilds[0].voice_channels
    
    await ctx.send("_____Listing Channels_____")

    if len(channels) == 0:
        await ctx.send("/No Channels/")
    else:
        for channel in channels:
            await ctx.send(f"{channel}")
    
    await ctx.send("~")

@client.command()
async def list_channel_members(ctx, *, channel_name):
    channels: List = client.guilds[0].voice_channels

    member_list: List = []

    for channel in channels:
        if channel.name == channel_name:
            member_list = channel.members


    await ctx.send("____Listing Channel Members____")
    if len(member_list) == 0:
        await ctx.send(f"/Channel Empty/")
    else:
        for member in member_list:
            await ctx.send(f"{member.nick}")
    await ctx.send("~")

client.run(TOKEN)