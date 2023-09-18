import os
import sys
import settings
import discord
import random
from discord.ext import commands
from string import ascii_lowercase, digits
from random import choice, shuffle

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=['!'], intents=intents)

# START // ADMIN    
    @bot.event
    async def on_ready():
        print(f"We're online baby!")
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        
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

# START // FUN Commands
    @bot.hybrid_command(
        aliases=['p'],
        help="Simple ping pong game",
        description="Answers with pong",
        brief="Ping pong!"
    )
    async def ping(ctx):
        await ctx.send("pong")  
              
    @bot.hybrid_command(
        aliases=['8ball','magic8ball'],
        help="Help description",
        description="Long description",
        brief="Short description"
    )
    async def eightball(ctx, *,question):
        responses=["Yes","No","Maybe","Reply hazy, try again","Don't count on it","Outlook is good","Signs point to yes","Concentrate and ask again","Cannot predict now","Ask again later","My sources say no","Very doubtful"]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
# END // FUN Commands
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()