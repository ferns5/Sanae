import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} logged in!')

@bot.slash_command(name="ping", description="pong")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("Pong ᗜˬᗜ ")

bot.run(TOKEN)
