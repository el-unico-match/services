from configs.settings import settings
from repository.servicesMetadata import ApiServicesTypes

async def status():
    return { 
        "name": "",
        "type": ApiServicesTypes.SERVICE.value,
        "site": settings.APP_SITE,
        "version": settings.APP_VERSION,
        "startupTime": settings.INIT_TIME,
        "apikey_status": settings.apikey_status,
        "apikeys_count": len(settings.apikey_whitelist),
    }
