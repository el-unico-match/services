from fastapi import APIRouter, status
from repository.servicesMetadata import ApiService

from endpoints.postService import PostServiceRequest, PostServiceResponse, postService
from endpoints.putService import putServiceRequest, putService
from endpoints.getService import getService
from endpoints.deleteService import deleteService
from endpoints.getServices import getServices
from endpoints.getTypes import getTypes
from endpoints.getAvailabilities import getAvailabilities

router=APIRouter()

@router.get(
    path="/types",
    summary="Returns a list of types.",
    tags=["services types"], 
    status_code=status.HTTP_200_OK,
    )
async def types():
    return await getTypes()

@router.get(
    path="/availabilities",
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
    status_code=status.HTTP_201_CREATED,
    )
async def post(request: PostServiceRequest) -> PostServiceResponse:
    """
    - **type**: type of service
    - **baseUrl**: url where the service is available
    - **version**: hash from the last commit from the service
    - **availability**: describes wether the key should be operational or not
    """
    return await postService(request)

@router.put(
    path="/services/{id}",
    summary="Updates an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def put(id: str, request: putServiceRequest) -> ApiService:
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
    return await putService(id, request)

@router.get(
    path="/services/{id}",
    summary="Fetch an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def get(id: str) -> ApiService:
    """
    - **id**: id of an existent service
    """
    return await getService(id)

@router.delete(
    path="/services/{id}",
    summary="Deletes an existing service.",
    tags=["services"],
    status_code=status.HTTP_200_OK,
    )
async def delete(id: str):
    """
    - **id**: id from deleted service
    """
    return await deleteService(id)

@router.get(
    path="/services/", 
    summary="Returns a list of services.", 
    tags=["services"], 
    status_code=status.HTTP_200_OK)
async def list():
    return await getServices()
