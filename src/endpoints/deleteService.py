
from repository.servicesMetadata import ApiService
from repository.serviceRepository import ServiceRepository

async def deleteService(id: str) -> str:
    return await ServiceRepository.deleteItem(id)