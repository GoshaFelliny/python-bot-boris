
settings = {
    'token': 'OTY2NDA4MzYzMDMyMzI2MTQ1.GxegGD.wGPaPf7Sq-NxtuhEEEV3oLYMI98abNQQNXGNBQ', #Токен
    'bot': 'Boris', #Имя бота
    'id': 966408363032326145, #ID бота
    'prefix': '>', #Префикс для команд
    'main_channel': 765270981395611649 #ID Основного канала, для отправки сообщений
}

private = {
    'category': 648144841364078607,
    'channel': 980779793257750569
}

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
