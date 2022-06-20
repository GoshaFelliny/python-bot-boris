from discord_components import Button, ButtonStyle

ButtonForAut1 = Button(style=ButtonStyle.URL, label='VK', emoji='🐷', url='https://vk.com/gogamencov')
ButtonForAut2 = Button(style=ButtonStyle.URL, label='STEAM', emoji='⚙',
                       url='https://steamcommunity.com/id/GoshaFelliny/')
ButtonForAut3 = Button(style=ButtonStyle.URL, label='GitHub', emoji='🐈‍⬛', url='https://github.com/GoshaFelliny')

BtnAut = [ButtonForAut1, ButtonForAut2, ButtonForAut3]

ButtonPlay1 = Button(style=ButtonStyle.green, label='', emoji='❌')
ButtonPlay2 = Button(style=ButtonStyle.red, label='', emoji='🔘')

BtnPlay = [ButtonPlay1, ButtonPlay2]
