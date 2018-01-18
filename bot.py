import discord
import asyncio
import secret
import diceroller

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {}".format(client.user.name))

@client.event
async def on_message(message):
    if message.content.lower().startswith('!roll'):
        args = message.content[6:]
        print("Rolling {args} for {client}...".format(args=args, client=message.author))
        roll = diceroller.roll_detailed(args)
        await client.send_message(message.channel, str(roll))
    if "monster" in message.content:
        await client.send_message(message.channel, ":japanese_ogre:")


client.run(secret.bot_token)

