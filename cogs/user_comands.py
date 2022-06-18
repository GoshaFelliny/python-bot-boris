import discord
from UserInterface import UI_Discord
import random
from discord.ext import commands


class User(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #бот включен
    @commands.Cog.listener()
    async def on_ready(self):
        print("Boris connected!")


    #бросок кубика
    @commands.command()
    async def dice(self, ctx):
        author = ctx.message.author
        dice1 = random.randint(1, 6)
        await ctx.send(f'{author.mention} выбросил {dice1} 🎲')


    #очистка сообщений
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, *, amout):
        lim = int(amout)
        await ctx.channel.purge(limit=lim)


    #информация о разработчике
    @commands.command()
    async def author(self, ctx):
        await ctx.send(components=[UI_Discord.BtnAut])



    #кик на сервере
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, **reason):
        try:
            await ctx.send(f'{member} кикнут по причине {reason}')
            await member.kick()

        finally:
            await ctx.send("You don`t have permmision")


    #бан на сервере
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, member: discord.Member, *reason):
        try:
            await ctx.send(f'{member} забанен по причине {reason}')
            await member.ban()

        finally:
            ctx.send("You don`t have permmision")


    #получение id роли (только для разработчка)
    @commands.command()
    async def getrole(self, ctx, role: discord.Role):
        if ctx.author.id == 299829027571761153:
            await ctx.send(role.id)

        else:
            await ctx.send("You don`t have permmision")

    # информация о сервере
    @commands.command()
    async def server(self, ctx):
        embed = discord.Embed(
            description=f'**Информация о сервере** **{ctx.guild.name}**\n'
                        f'\n'
                        f'**Участники:**\n'
                        f'Людей: **{ctx.guild.member_count}**\n'
                        f'\n'
                        f'**Каналы:**\n'
                        f'💬 Текствые: **{len(ctx.guild.text_channels)}**\n'
                        f'🔊 Голосовые: **{len(ctx.guild.voice_channels)}**\n'
                        f'▶  Категории: **{len(ctx.guild.categories)}**\n'
                        f'\n'
                        f'**Владелец:**\n'
                        f'{ctx.guild.owner}\n'
                        f'\n'
                        f'**Уровень проверки:**\n'
                        f'{ctx.guild.verification_level}\n'
                        f'**Дата создания:**\n{ctx.guild.created_at.strftime("%d.%m.%Y")}\n',
            color=ctx.author.color, )
        embed.set_footer(text=f'ID: {ctx.guild.id}')
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        await ctx.send(embed=embed)


    # помощь
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            description=
                            f'\n'
                            f'**Комнады:**\n'
                            f'>server - информация о сервере\n'
                            f'>ban [ник] [причина] - бан участника\n'
                            f'>kick [ник] [причина] - кик участника\n'
                            f'>dice - бросок кубика\n'
                            f'>clear [число] - очистка сообщений в канале \n'
                            f'>song [ссылка с ютуба] - проигрыш музыки\n'
                            f'>stop - остановка музыки\n'
                            f'>create_private - создания категории с приватными комнатами',
            
            сolor=ctx.author.color)
        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(User(bot))
