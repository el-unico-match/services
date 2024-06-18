from configs.settings import settings
from repository.servicesMetadata import ApiServicesTypes

async def status():
    return { 
        "name": "",
        "type": ApiServicesTypes.SERVICES.value,
        "site": settings.APP_SITE,
        "version": settings.APP_VERSION,
        "startupTime": settings.INIT_TIME,
    }
