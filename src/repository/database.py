from typing import Any
from configs.settings import settings
from pymongo import MongoClient # type: ignore

from exceptions.NotFoundException import NotFoundException

class DatatabaseClient:
   
  client: MongoClient
  database: any

  def __init__(self, collectionName: str):
    self.client = MongoClient(settings.db_url)
    self.database = self.client.db[collectionName]

  def close(self):
    self.client.close()

  @staticmethod
  def init():
    client=DatatabaseClient('services')
    client.createUniqueIndex('baseUrl')
    client.close()

  @staticmethod
  def get_services_instance():
      databaseClient = DatatabaseClient('services')
      try:
          yield databaseClient
      finally:
          databaseClient.close()

  def createUniqueIndex(self, columnName):
    self.database.create_index(
      keys=columnName,
      unique=True,
      background=True,
    )

  def testConnection(self) -> bool:
     self.database.command('ping')
     return True

  async def persistItem(self, item: Any) -> Any: 
    result=self.database.insert_one(document=item.__dict__)

    if ( result.acknowledged == False):
      raise Exception('Failed')

    return result.inserted_id

  async def retrieveItem(self,id: str) -> Any: 
    result=self.database.find_one(filter={'id': id})

    if ( result == None):
      raise NotFoundException('No se encontró el elemento')

    del result['_id']

    return result

  async def filterItems(self, filter: any) -> Any: 
    result=self.database.find(filter=filter, projection={'_id': False})
    data =list(result)

    return data

  async def filterItem(self, filter: any) -> Any: 
    result=self.database.find_one(filter=filter)

    if ( result == None):
      raise NotFoundException('No se encontró el elemento')

    del result['_id']

    return result

  async def updateItem(self, item: Any) -> Any:

    data=dict(item.__dict__)
    result=self.database.find_one_and_replace(filter={'id':item.id}, replacement=data, projection={'_id': False}, upsert=False)
    
    if ( result == None):
      raise NotFoundException('No se encontró el elemento')
    
    return result

  async def deleteItem(self,id: str) -> id:
    result=self.database.find_one_and_delete(filter={'id': id},projection={'_id': False})

    if ( result == None):
      raise NotFoundException('No se encontró el elemento')
    
    return result

  async def listItems(self, filter={}) -> id:
    result=self.database.find(filter=filter, projection={'_id': False})
    data =list(result)

    return data
