from typing import Any
from configs.EnvSettingsLoader import settings
from pymongo import MongoClient

from exceptions.NotFoundException import NotFoundException

mongoClient = MongoClient(host=settings.DB_HOST,port=settings.DB_PORT)
print(mongoClient.host)

async def persistItem(collectionName: str, item: Any) -> Any: 
  result=mongoClient.db[collectionName].insert_one(document=item.__dict__)

  if ( result.acknowledged == False):
    raise Exception('Failed')

  return result.inserted_id

async def retrieveItem(collectionName: str,id: str) -> Any: 
  result=mongoClient.db[collectionName].find_one(filter={'id': id})

  if ( result == None):
    raise NotFoundException('No se encontró el elemento')

  del result['_id']

  return result

async def updateItem(collectionName: str, item: Any) -> Any:

  data=dict(item.__dict__)
  result=mongoClient.db[collectionName].find_one_and_replace(filter={'id':item.id}, replacement=data, projection={'_id': False}, upsert=False)
  
  if ( result == None):
    raise NotFoundException('No se encontró el elemento')
  
  return result

async def deleteItem(collectionName: str,id: str) -> id:
  result=mongoClient.db[collectionName].find_one_and_delete(filter={'id': id},projection={'_id': False})

  if ( result == None):
    raise NotFoundException('No se encontró el elemento')
  
  return result

async def listItems(collectionName: str) -> id:
  result=mongoClient.db[collectionName].find(filter={}, projection={'_id': False})
  data =list(result)

  return data
