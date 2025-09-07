import discord
from discord.ext import commands
import os

# Botのトークンは環境変数から取得
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を扱う場合は必須

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ ログイン完了: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

bot.run(TOKEN)
