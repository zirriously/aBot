import discord
import asyncio
import os

token = open("token.txt", "r").read()
channelID = open("channelid.txt", "r").read()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in with " + token + ", listening for messages on " + channelID)

@client.event
async def on_message(message):
    if message.channel.id == channelID and message.content.startswith("."):
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        await message.add_reaction("🔴")
        print("Added reactions to - " + message.content)


client.run(token)
