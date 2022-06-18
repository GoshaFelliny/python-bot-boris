import discord
from settings.config_local import YDL_OPTIONS, FFMPEG_OPTIONS
from discord.ext import commands
from youtube_dl import YoutubeDL

class Music(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot


    @commands.command()
    async def song(self, ctx, *, arg):
        vc = await ctx.message.author.voice.channel.connect()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in arg:
                info = ydl.extract_info(arg, download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

        url = info['formats'][0]['url']

        await ctx.send(f'Boris play now: {arg}')
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=url, **FFMPEG_OPTIONS))


    #отключения бота
    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.message.delete()
        await ctx.send(f'Проигрышь остановлен')




def setup(bot):
    bot.add_cog(Music(bot))
