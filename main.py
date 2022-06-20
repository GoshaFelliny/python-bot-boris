from start.bot import bot
from settings.config_local import settings

if __name__ == '__main__':
    bot.run(settings['token'])
