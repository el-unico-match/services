
from repository.servicesMetadata import ApiService
from repository.serviceRepository import ServiceRepository

async def getService(id: str) -> ApiService:
    return await ServiceRepository.retrieveItem(id)