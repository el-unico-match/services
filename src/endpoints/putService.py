import asyncio
from pydantic import Field, BaseModel
from typing import Optional
from repository.servicesMetadata import ApiService, ApiServicesStatus, ApiServicesTypes
from repository.database import DatatabaseClient
from common.WhiteListHelper import spreadWhiteList

class putServiceRequest(BaseModel):
   id: str = Field()
   type: ApiServicesTypes = Field()
   key: str = Field()
   baseUrl: str = Field()
   version: Optional[str] = Field()
   availability: ApiServicesStatus = Field()

async def putService(id: str, request: putServiceRequest, databaseClient: DatatabaseClient) -> ApiService: 
   
   result = await databaseClient.retrieveItem(id)
   result['type']=request.type
   result['key']=request.key
   result['baseUrl']=request.baseUrl
   result['version']=request.version
   result['availability']=request.availability

   apiService = ApiService(**result)
   await databaseClient.updateItem(apiService)
   
   asyncio.create_task(spreadWhiteList(databaseClient))

   return apiService
    