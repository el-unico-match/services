from configs.EnvSettingsLoader import SettingsLoader
from repository.servicesMetadata import ApiServicesTypes

Settings=SettingsLoader()

async def status():
    return { 
        "name": "",
        "type": ApiServicesTypes.SERVICES.value,
        "site": Settings.APP_SITE,
        "version": Settings.APP_VERSION,
        "startupTime": Settings.INIT_TIME,
    }
