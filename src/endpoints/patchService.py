from datetime import datetime, timezone
from pydantic import BaseModel, Field
from repository.servicesMetadata import ApiService, ApiServicesStatus
from dataclasses import dataclass
from repository.database import DatatabaseClient
from exceptions.NotFoundException import NotFoundException
from exceptions.ForbiddenException import ForbiddenException

@dataclass
class PatchServiceRequest(BaseModel):
   availability: ApiServicesStatus = Field()

@dataclass
class PatchServiceResponse():
   id: str
   type: str
   key: str
   token: str
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
      key = extractKey(apiKey)

      # token should be validated here, only filtering by admin users

      if ( data['key'] != key or (userToken != None  or (baseUrl != None and data['baseUrl'] != baseUrl)) ):
         raise ForbiddenException('Invalid ApiKey, token or baseUrl')  

   except:
      raise ForbiddenException('')
   
   apiService=ApiService(**data)
   apiService.availability = request.availability
   apiService.updated=datetime.now(timezone.utc)
   await databaseClient.updateItem(apiService)

   response = PatchServiceResponse(
      id = apiService.id,
      type = apiService.type,
      key = apiService.key,
      token = apiKey,
      baseUrl= apiService.baseUrl,
      version= apiService.version,
      created=apiService.created,
      updated=apiService.updated,
      availability=apiService.availability,
   )

   return response
