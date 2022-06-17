import discord
import random
from discord_components import DiscordComponents, Button, ButtonStyle



#Кнопки для команды >author
ButtonForAut1 = Button(style = ButtonStyle.URL, label = 'VK', emoji = '🐷', url = 'https://vk.com/gogamencov')
ButtonForAut2 = Button(style = ButtonStyle.URL, label = 'STEAM', emoji = '⚙', url = 'https://steamcommunity.com/id/GoshaFelliny/')
ButtonForAut3 = Button(style = ButtonStyle.URL, label = 'GitHub', emoji = '🐈‍⬛', url = 'https://github.com/GoshaFelliny')

BtnAut = [ButtonForAut1, ButtonForAut2, ButtonForAut3]


#Кнопки для команды play

ButtonPlay1 = Button(style = ButtonStyle.green, label = '', emoji = '❌')
ButtonPlay2 = Button(style = ButtonStyle.red, label = '', emoji = '🔘')

BtnPlay = [ButtonPlay1, ButtonPlay2]