
import asyncio
from repository.database import DatatabaseClient
from common.WhiteListHelper import spreadWhiteList

async def deleteService(id: str, databaseClient: DatatabaseClient) -> str:
   result = await databaseClient.deleteItem(id)
   asyncio.create_task(spreadWhiteList(databaseClient))
   return result;
