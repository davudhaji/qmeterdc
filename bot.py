# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import time
load_dotenv()

token = os.getenv('TOKEN')
print(token,'TOKEN')
intents = discord.Intents().all()
# intents.members = True
# intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user.name}')

@bot.command()
async def ping(ctx):
    start_time = time.time()
    message = await ctx.send("Pinging...")
    end_time = time.time()

    latency = round((end_time - start_time) * 1000, 2)  # Latency in milliseconds

    await message.edit(content=f"Pong! Bot Latency: {bot.latency * 1000} ms | Member Latency: {latency} ms")




@bot.command()
async def status(ctx):
    guild = ctx.guild
    members = guild.members
    print()
    for member in members:
        message = f"{member.name}: {member.status}"
        await ctx.send(message)



@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(guild.text_channels, name="qmeter")
    if channel:
        message = f"{member.mention} xoş gəldin! Qmeterə qatıldığın üçün təşəkkür edirik."
        await channel.send(message)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



bot.run(token)  