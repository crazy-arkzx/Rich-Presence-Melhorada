# SISTEMA DE RICH PRESENCE PARA SEU BOT
# FEITO POR: Crazy_ArKzX
# GitHub: https://github.com/crazy-arkzx

import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    servidores = len(bot.guilds)
    usuarios = sum(guild.member_count for guild in bot.guilds)

    await bot.change_presence(
        activity=discord.Game(
            name=f"Em {servidores} Servidores e Auxiliando {usuarios} Usuários"
        )
    )
    print("Rich Presence Carregada com Sucesso!")

bot.run("SEU_TOKEN")