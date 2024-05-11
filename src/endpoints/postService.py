from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from repository.servicesMetadata import ApiService, ApiServicesStatus, ApiServicesTypes
from repository.serviceRepository import ServiceRepository
from dataclasses import dataclass

@dataclass
class PostServiceRequest(BaseModel):
   type: ApiServicesTypes = Field()
   baseUrl: str = Field()
   version: Optional[str] = Field()
   availability: ApiServicesStatus = Field()

async def postService(request: PostServiceRequest) -> ApiService: 
   data=request.model_dump()   
   data["key"]="key"
   data["created"]=datetime.now()
   data["id"]=str(ObjectId())

   apiService=ApiService(**data)
   await ServiceRepository.persistItem(apiService)
   
   return apiService
    