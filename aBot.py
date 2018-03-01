import discord
import asyncio
import os

token = open("token.txt", "r").read()

client = discord.Client

@client.event
async def on_ready():
    print("logged in...")

client.run(token)
