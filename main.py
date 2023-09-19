import settings
from settings import os, sys, random, string, aiohttp, re
import filters
import discord
from discord.ext import commands
from discord.ext.commands import bot, has_permissions, MissingPermissions, is_owner
from discord.utils import get
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
import json

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=['!'], intents=intents)

# START // ADMIN    
    @bot.event
    async def on_ready():
        print(f"We're online baby!")
        logger.info(f"User: {bot.user} (ID: {bot.user.id})") # type: ignore
        
    @bot.hybrid_command(
        help="Syncs slash commands to server",
        description="Sync slash commands",
        brief="Slash command sync"
    )
    async def sync(ctx):
        print("sync command")
        if ctx.author.id == 372450113655799810:
            await bot.tree.sync()
            await ctx.send('Command tree synced.')
        else:
            await ctx.send('You must be the owner to use this command!')    
    
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)

    @bot.command(
        name= 'restart',
        help="Restarts the bot",
        description="Restarts the bot",
        brief="Bot restart"
    )
    async def restart(ctx):
        if discord.utils.get(ctx.author.roles, name="Moderator"):
            await ctx.send("Restarting bot...")
            restart_bot()
        if ctx.author.id == 372450113655799810:
            await ctx.send("Restarting bot...")
            restart_bot()
        else:
            await ctx.send('You must be the owner to use this command!')
# END // ADMIN
            
# START // Slash Command Template        
#    @bot.hybrid_command(
#        aliases=['t'],
#        help="Help description",
#        description="Long description",
#        brief="Short description"
#    )
#    async def test(ctx):
#        await ctx.send("This is a hybrid command!")
# END // Slash Command Template

# START // No Prefix Commands
    @bot.event
    async def on_message(message):
        if message.author == bot.user:  # skip bot messages
            return
 
        if message.content.lower() in filters.greetings:
            await message.reply('Yo! Sup?')
 
        if message.content.lower() in filters.suspect_words:
            await message.channel.send(f"{message.author.mention} https://media.tenor.com/KO81J6pNN2AAAAAC/back-away.gif")
                   
        if message.content.lower() in filters.filtered_words:
            await message.delete()
            await message.channel.send(f"{message.author.mention} The fucks wrong with you?")

        await bot.process_commands(message)  # to allow other commands
# End // No Prefix Commands

# START // FUN Commands

    @bot.hybrid_command(
        aliases=['p'],
        help="Simple ping pong game",
        description="Answers with pong",
        brief="Ping pong!"
    )
    async def ping(ctx):
        """ Answers with pong """
        await ctx.send("pong")  
              
    @bot.hybrid_command(
        aliases=['8ball','magic8ball'],
        help="Help description",
        description="Long description",
        brief="Short description"
    )
    async def eightball(ctx, *, question):
        responses=["Yes","No","Maybe","Reply hazy, try again","Don't count on it","Outlook is good","Signs point to yes","Concentrate and ask again","Cannot predict now","Ask again later","My sources say no","Very doubtful"]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
        
    @bot.hybrid_command(
        aliases=['simonsays'],
        help="Help description",
        description="Long description",
        brief="Short description"
    )
    async def says(ctx, *what):
        """ Game of Simon Says """
        await ctx.send(" " .join(what)) 
        
# END // FUN Commands
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True) # type: ignore

if __name__ == "__main__":
    run()