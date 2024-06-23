from datetime import datetime, timezone
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from repository.servicesMetadata import ApiService, ApiServicesStatus, ApiServicesTypes
from dataclasses import dataclass
from common.JwtHelper import createToken
from repository.database import DatatabaseClient

@dataclass
class PostServiceRequest(BaseModel):
   type: ApiServicesTypes = Field()
   baseUrl: str = Field()
   version: Optional[str] = Field()

@dataclass
class PostServiceResponse():
   id: str
   type: str
   key: str
   apiKey: str
   baseUrl: str
   version: str
   created: datetime
   updated: datetime
   availability: str

async def postService(request: PostServiceRequest, databaseClient: DatatabaseClient) -> PostServiceResponse: 

   id=str(ObjectId())

   apiKey=createToken(id, request.baseUrl, request.type.value)

   jwtParts=apiKey.split('.')
   now=datetime.now(timezone.utc)

   data=request.model_dump()   
   data["id"]=id
   data["created"]=now
   data["updated"]=now
   data["apiKey"]=apiKey
   data["key"]=jwtParts[1][:6]
   data["availability"]=ApiServicesStatus.DISABLED

   apiService=ApiService(**data)
   await databaseClient.persistItem(apiService)
   
   response=PostServiceResponse(
      id=apiService.id,
      type=apiService.type.value,
      key=apiService.key,
      apiKey=apiKey,
      baseUrl=apiService.baseUrl,
      version=apiService.version,
      created=apiService.created,
      updated=apiService.updated,
      availability=apiService.availability.value,
   )
   
   return response
    