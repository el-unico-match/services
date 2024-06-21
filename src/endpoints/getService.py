
from repository.servicesMetadata import ApiService
from repository.database import DatatabaseClient

async def getService(id: str, databaseClient: DatatabaseClient) -> ApiService:
    return await databaseClient.retrieveItem(id)