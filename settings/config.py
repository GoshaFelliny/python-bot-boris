try:
    from config_local import *
except ModuleNotFoundError as err:
    print('Локальные настройки не найдены')