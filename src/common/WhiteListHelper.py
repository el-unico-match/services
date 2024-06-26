import httpx
import logging
from repository.database import DatatabaseClient
from configs.settings import settings
from fastapi.encoders import jsonable_encoder

async def spreadWhiteList(databaseClient: DatatabaseClient):
    logger=logging.getLogger(__name__)

    try:
        allRegisteredServices = await databaseClient.filterItems({})
        enabledServices = list(filter(lambda x: x['availability'] == 'enabled', allRegisteredServices))

        data={
            'apiKeys': list([item['apiKey'] for item in enabledServices])
        }
    
        for service in allRegisteredServices:
            url = f"{service['baseUrl']}/whitelist"
            headers={"x-apikey": settings.apikey_value }
            async with httpx.AsyncClient() as client:
                try: 
                    response = await client.put(url, headers=headers, json=data)

                    if ( response.status_code == 201):
                        logger.info(f"apikey enabled in {service['type']} - {service['baseUrl']}") 

                    else:
                        logger.error(f"Error while sending whitelist: {str(response.status_code): jsonable_encoder(response)}")

                except Exception:
                    logger.error(f"Error while sending whitelist", exc_info=True)    

    except Exception as exception:
        logger.error(f"Error while creationg whitelist", str(exception), exc_info=True)

