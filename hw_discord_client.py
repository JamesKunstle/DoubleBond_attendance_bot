# bot.py
import os

import discord
from dotenv import load_dotenv

def ping_client():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    client.run(TOKEN)

    return

def ping_client_guild():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client()

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    client.run(TOKEN)

    return


def get_guild_members():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    client = discord.Client() #this points to the Double Bond bot

    @client.event
    async def on_ready():
        for guild in client.guilds: # client.guilds refers to the guilds that the Double_Bond bot belongs to.
            if guild.name == GUILD:
                print("guild found")
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    client.run(TOKEN)

    return

def list_members():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    CHANNEL = os.getenv('BROTHER_CHAT_CHANNEL')

    client = discord.Client()

    @client.event
    async def on_ready():

        for guild in client.guilds:
            if guild.name == GUILD:
                break
        
        for channel in guild.voice_channels:
            if channel.name == CHANNEL:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

        members = '\n - '.join(["person in chat" for member in channel.members])
        print(f'Members in Brother Chat:\n - {members}')

    client.run(TOKEN)

    return




def main():
    #ping_client()
    #ping_client_guild()
    get_guild_members()
    #list_members()

if __name__ == "__main__":
    main()