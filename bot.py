# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

token = os.getenv('TOKEN')
print(token,'TOKEN')
intents = discord.Intents.default()
intents.typing = False  # Yazma olayları için intents'i devre dışı bırakabilirsiniz
intents.presences = False  # Durum olayları için intents'i devre dışı bırakabilirsiniz

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user.name}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(guild.text_channels, name="qmeter")
    if channel:
        message = f"{member.mention} xoş gəldin! Qmeterə qatıldığın üçün təşəkkür edirik."
        await channel.send(message)

bot.run(token)  