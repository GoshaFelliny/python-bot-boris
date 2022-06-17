import discord
import os
from pathlib import Path
from discord.ext import commands
from settings.config_local import settings

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = settings['prefix'],  intents=intents)
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 299829027571761153:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Load successfully')

    else:
        await  ctx.send('You don`t have permission')

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 299829027571761153:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send('Unload successfully')

    else:
        await  ctx.send('You don`t have permission')

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 299829027571761153:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Reboot successful')

    else:
        await  ctx.send('You don`t have permission')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run(settings['token'])