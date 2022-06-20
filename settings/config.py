settings = {
    'token': 'BAD_TOKEN',
    'bot': 'BAD_NAME',
    'id': 'BAD_ID',
    'prefix': 'BAD_PREFIX',
}
YDL_OPTIONS = 'BAD_YDL_OPTIONS'
FFMPEG_OPTIONS = 'BAD_FFMPEG_OPTIONS'

try:
    from config_local import *
except ModuleNotFoundError as err:
    print('Локальные настройки не найдены')
