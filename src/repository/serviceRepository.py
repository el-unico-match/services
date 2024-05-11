from typing import Any
from repository.database import deleteItem, listItems, persistItem, retrieveItem, updateItem

class ServiceRepository():

    collection = "services"

    @staticmethod
    async def persistItem(item):
        return await persistItem(ServiceRepository.collection, item)
    
    @staticmethod
    async def retrieveItem(id: str):
        return await retrieveItem(ServiceRepository.collection, id)
    
    @staticmethod
    async def updateItem(item: Any):
        return await updateItem(ServiceRepository.collection, item)
    
    @staticmethod
    async def deleteItem(id: str):
        return await deleteItem(ServiceRepository.collection, id) 
    
    @staticmethod
    async def listItems():
        return await listItems(ServiceRepository.collection) 