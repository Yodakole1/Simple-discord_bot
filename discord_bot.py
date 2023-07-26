import discord
import odgovori
import json

botfile = 'BOT_API'
api_key = {}
with open(botfile, 'r') as f:
    api_key = json.loads(f.read())

async def poslata_poruka(poruka, user_poruka, is_private):
    try:
        odgovor = odgovori.get_odgovor(user_poruka)
        await poruka.author.send(odgovori) if is_private else await poruka.channel.send(odgovor)

    except Exception as e:
        print(e)


def run_bot():
    TOKEN = api_key["MAINAPI"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    
    
    @client.event
    async def on_message(poruka):
        if poruka.author == client.user:
            return

        ime = str(poruka.author)
        user_poruka = str(poruka.content)
        channel = str(poruka.channel)

        print(f'{ime} rekao : "{user_poruka}" ({channel})')

        if user_poruka[0] == '?':
            user_poruka = user_poruka[1:]
            await poslata_poruka(poruka, user_poruka, is_private=True)
        else:
            await poslata_poruka(poruka, user_poruka, is_private=False)

    client.run(TOKEN)
