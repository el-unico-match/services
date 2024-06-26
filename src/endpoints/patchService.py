import asyncio
from configs.settings import settings
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from repository.servicesMetadata import ApiService, ApiServicesStatus
from dataclasses import dataclass
from repository.database import DatatabaseClient
from exceptions.NotFoundException import NotFoundException
from exceptions.ForbiddenException import ForbiddenException
from common.WhiteListHelper import spreadWhiteList

@dataclass
class PatchServiceRequest(BaseModel):
   availability: ApiServicesStatus = Field()

@dataclass
class PatchServiceResponse():
   id: str
   type: str
   key: str
   apiKey: str
   baseUrl: str
   version: str
   created: datetime
   updated: datetime
   availability: str

def extractKey(apiKey: str) -> str:
   try:
      return apiKey.split('.')[1][:6]
   
   except:
      raise NotFoundException("Invalid Api Key")

async def patchService(id: str, apiKey: str | None, userToken: str | None, baseUrl: str, request: PatchServiceRequest, databaseClient: DatatabaseClient) -> PatchServiceResponse: 

   data = await databaseClient.retrieveItem(id)

   try:
      if ( (data['apiKey'] == apiKey or apiKey in settings.apikey_whitelist) == False):
         raise ForbiddenException('Invalid ApiKey, token or baseUrl')  

   except:
      raise ForbiddenException('')
   
   apiService=ApiService(**data)
   apiService.availability = request.availability
   apiService.updated=datetime.now(timezone.utc)
   await databaseClient.updateItem(apiService)

   asyncio.create_task(spreadWhiteList(databaseClient))

   response = PatchServiceResponse(
      id = apiService.id,
      type = apiService.type,
      key = apiService.key,
      apiKey = apiKey,
      baseUrl= apiService.baseUrl,
      version= apiService.version,
      created=apiService.created,
      updated=apiService.updated,
      availability=apiService.availability,
   )

   return response
