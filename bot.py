# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import youtube_dl

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


@bot.command()
async def play(ctx, url):
    voice_channel = ctx.message.author.voice.channel
    if voice_channel is None:
        await ctx.send("Önce bir sesli kanala katılmanız gerekiyor.")
        return
    voice_channel = await voice_channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        voice_channel.play(discord.FFmpegPCMAudio(url2))



bot.run(token)  