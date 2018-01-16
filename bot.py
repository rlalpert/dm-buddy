import discord
import asyncio
import secret

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {}".format(client.user.name))

@client.event
async def on_message(message):
    if "monster" in message.content:
        await client.send_message(message.channel, ":japanese_ogre:")


client.run(secret.bot_token)