
from typing import Any
from repository.serviceRepository import ServiceRepository

async def getServices() -> Any:
    return await ServiceRepository.listItems()