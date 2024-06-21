
from typing import Any
from repository.database import DatatabaseClient

async def getServices(databaseClient: DatatabaseClient) -> Any:
    return await databaseClient.listItems()