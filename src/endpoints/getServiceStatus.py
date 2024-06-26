import httpx
from configs.settings import settings
from repository.servicesMetadata import ApiService
from repository.database import DatatabaseClient

async def getServiceStatus(id: str, databaseClient: DatatabaseClient):
    async with httpx.AsyncClient() as client:
        service = await databaseClient.retrieveItem(id)

        try:
            headers={"x-apikey": settings.apikey_value }
            response = await client.get(f"{service['baseUrl']}/status", headers=headers)
            return response.status_code
        
        except Exception as e:
            return 500
    