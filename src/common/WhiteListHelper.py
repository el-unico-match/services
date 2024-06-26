import httpx
import logging
from repository.database import DatatabaseClient
from fastapi.encoders import jsonable_encoder

async def spreadWhiteList(databaseClient: DatatabaseClient):
    logger=logging.getLogger(__name__)

    try:
        enabledServices = await databaseClient.filterItems({'availability': 'enabled'})
        data={
            'apiKeys': list([item['apiKey'] for item in enabledServices])
        }
    
        for service in enabledServices:
            url = f"{service['baseUrl']}/whitelist"
            async with httpx.AsyncClient() as client:
                try: 
                    response = await client.put(url, json=data)

                    if ( response.status_code == 201):
                        logger.info(f"apikey enabled in {service['type']} - {service['baseUrl']}") 

                    else:
                        logger.error(f"Error while sending whitelist: {str(response.status_code): jsonable_encoder(response)}")

                except Exception as requestException:
                    logger.error(f"Error while sending whitelist", str(requestException), exc_info=True)    

    except Exception as error:
        logger.error(f"Error while creationg whitelist", str(error), exc_info=True)

