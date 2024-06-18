from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from repository.servicesMetadata import ApiService, ApiServicesStatus, ApiServicesTypes
from repository.serviceRepository import ServiceRepository
from dataclasses import dataclass
from common.JwtHelper import createToken

@dataclass
class PostServiceRequest(BaseModel):
   type: ApiServicesTypes = Field()
   baseUrl: str = Field()
   version: Optional[str] = Field()
   availability: ApiServicesStatus = Field()

@dataclass
class PostServiceResponse():
   id: str
   type: str
   key: str
   token: str
   baseUrl: str
   version: str
   created: datetime
   availability: str

async def postService(request: PostServiceRequest) -> PostServiceResponse: 

   token=createToken(request.baseUrl, request.type.value)

   jwtParts=token.split('.')

   data=request.model_dump()   
   data["key"]="key"
   data["created"]=datetime.now()
   data["id"]=str(ObjectId())
   data["key"]=jwtParts[1][:6]

   apiService=ApiService(**data)
   await ServiceRepository.persistItem(apiService)
   
   response=PostServiceResponse(
      id=apiService.id,
      type=apiService.type.value,
      key=apiService.key,
      token=token,
      baseUrl=apiService.baseUrl,
      version=apiService.version,
      created=apiService.created,
      availability=apiService.availability.value,
   )
   
   return response
    