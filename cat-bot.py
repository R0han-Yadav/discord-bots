import discord

TOKEN = "OTcxODA4MDU2ODg1MjY0NDM1.YnP4yA.KXAeH819LABpWMqfQpxxALnXFBQ"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is here!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("nya!")

client.run(TOKEN)
