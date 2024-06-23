from typing import Annotated, Optional
from fastapi import APIRouter, status, Depends, Request, Header
from repository.servicesMetadata import ApiService
from repository.database import DatatabaseClient
from exceptions.ValidationException import ValidationException

from endpoints.postService import PostServiceRequest, PostServiceResponse, postService
from endpoints.putService import putServiceRequest, putService
from endpoints.getService import getService
from endpoints.deleteService import deleteService
from endpoints.getServices import getServices
from endpoints.getTypes import getTypes
from endpoints.getAvailabilities import getAvailabilities
from endpoints.patchService import PatchServiceRequest, PatchServiceResponse, patchService

router=APIRouter()

@router.get(
    path="/services/types",
    summary="Returns a list of types.",
    tags=["services types"], 
    status_code=status.HTTP_200_OK,
    )
async def types():
    return await getTypes()

@router.get(
    path="/services/availabilities",
    summary="Returns a list of status.",
    tags=["services types"],
    status_code=status.HTTP_200_OK,
    )
async def types():
    return await getAvailabilities()

@router.post(
    path="/services",
    summary="Registers a new service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def post(request: PostServiceRequest, databaseClient = Depends(DatatabaseClient.get_services_instance)) -> PostServiceResponse:
    """
    - **type**: type of service
    - **baseUrl**: url where the service is available
    - **version**: hash from the last commit from the service
    """
    return await postService(request, databaseClient)

@router.put(
    path="/services/{id}",
    summary="Updates an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def put(id: str, request: putServiceRequest, databaseClient = Depends(DatatabaseClient.get_services_instance)) -> ApiService:
    """
    - **type**: type of service
    - // **key**: key assigned to service
    - **url**: url where the service is available
    - **port**: port to access the service
    - **version**: hash from the last commit from the service
    - **tag**: tag from the commit
    - **created**: date when it started operating
    - **availability**: describes wether the key should be operational or not
    """
    return await putService(id, request, databaseClient)

@router.patch(
    path="/services/{id}",
    summary="Updates an existing service availability.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
)
async def patch(id: str, request: Request, patchRequest: PatchServiceRequest , x_apiKey: Annotated[str | None, Header()] = None, x_token: Annotated[str | None , Header()] = None, databaseClient = Depends(DatatabaseClient.get_services_instance)) -> PatchServiceResponse:
    """
    - **apiKey**: key assigned to service
    - **baseUrl**: url where the service is available
    - **availability**: describes wether the key should be operational or not
    """
    baseUrl=f"{request.base_url.scheme}://{request.base_url.netloc}"

    if ( x_apiKey == None and x_token == None ):
        raise ValidationException('x_apiKey or x_token should is required')

    return await patchService(id, x_apiKey, x_token, baseUrl, patchRequest, databaseClient)

@router.get(
    path="/services/{id}",
    summary="Fetch an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def get(id: str, databaseClient = Depends(DatatabaseClient.get_services_instance)) -> ApiService:
    """
    - **id**: id of an existent service
    """
    return await getService(id, databaseClient)

@router.delete(
    path="/services/{id}",
    summary="Deletes an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def delete(id: str, databaseClient = Depends(DatatabaseClient.get_services_instance)):
    """
    - **id**: id from deleted service
    """
    return await deleteService(id, databaseClient)

@router.get(
    path="/services", 
    summary="Returns a list of services.", 
    tags=["services"], 
    status_code=status.HTTP_200_OK)
async def list(databaseClient = Depends(DatatabaseClient.get_services_instance)):
    return await getServices(databaseClient)
