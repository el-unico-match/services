
from repository.database import DatatabaseClient

async def deleteService(id: str, databaseClient: DatatabaseClient) -> str:
    return await databaseClient.deleteItem(id)