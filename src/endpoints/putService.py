from pydantic import Field, BaseModel
from typing import Optional
from repository.servicesMetadata import ApiService, ApiServicesStatus, ApiServicesTypes
from repository.serviceRepository import ServiceRepository

class putServiceRequest(BaseModel):
   id: str = Field()
   type: ApiServicesTypes = Field()
   key: str = Field()
   baseUrl: str = Field()
   version: Optional[str] = Field()
   availability: ApiServicesStatus = Field()

async def putService(id: str, request: putServiceRequest) -> ApiService: 
   
   result = await ServiceRepository.retrieveItem(id)
   result['type']=request.type
   result['key']=request.key
   result['baseUrl']=request.baseUrl
   result['version']=request.version
   result['availability']=request.availability

   apiService = ApiService(**result)
   await ServiceRepository.updateItem(apiService)
   
   return apiService
    