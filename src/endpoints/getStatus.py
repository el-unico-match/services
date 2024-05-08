from configs.EnvSettingsLoader import SettingsLoader

Settings=SettingsLoader()

async def status():
    return { 
        "name": "",
        "type": "service",
        "site": Settings.APP_SITE,
        "version": Settings.APP_VERSION,
        "startupTime": Settings.INIT_TIME,
    }
