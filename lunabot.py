import discord
import responses

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE1MzEwOTkzMzAyNjQ2MzgxNA.GwvwiM.r6edkqm67y_XNJS0dREcAowDBh0ndCnnmYEyu0'
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Yo! What\'s up?')

    client.run(TOKEN)