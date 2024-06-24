
from repository.database import DatatabaseClient
from common.WhiteListHelper import spreadWhiteList

async def deleteService(id: str, databaseClient: DatatabaseClient) -> str:
    result = await databaseClient.deleteItem(id)
    await spreadWhiteList(databaseClient)
    return result;