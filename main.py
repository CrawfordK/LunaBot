import os
import sys
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=['/','$','!'], intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        
    @bot.command()
    async def sync(ctx):
        print("sync command")
        if ctx.author.id == 372450113655799810:
            await bot.tree.sync()
            await ctx.send('Command tree synced.')
        else:
            await ctx.send('You must be the owner to use this command!')
        
    @bot.hybrid_command()
    async def test(ctx):
        await ctx.send("This is a hybrid command!")

    @bot.hybrid_command()
    async def ping(ctx):
        await ctx.send("pong")
    
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)

    @bot.command(name= 'restart')
    async def restart(ctx):
        if ctx.author.id == 372450113655799810:
            await ctx.send("Restarting bot...")
            restart_bot()
        else:
            await ctx.send('You must be the owner to use this command!')
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()