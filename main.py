import discord
import asyncio
from discord.ext import commands, tasks

TOKEN = "Enter your discord bot token here" # Enter Discord bot token here
USER_ID = {ENTER USER ID HERE} # Enter User ID here
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready(): # start when the code is run
    user = await bot.fetch_user(USER_ID)
    while True:
        await user.send(f"<@{USER_ID}>") # current content: @user, you can add whatever you want to it
        await asyncio.sleep(1) # Wait time, suggest change to 1 second or over. If not, may result in rate limited
bot.run(TOKEN)
