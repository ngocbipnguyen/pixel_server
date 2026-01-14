from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.collection_repo_impl import CollectionRepoImpl
from src.schemas.collection import Collection, CollectionParams, UpdateCollection, TimestampResponse
from src.schemas.response import APIResponse, ListResponse
from sqlalchemy.orm import Session
from src.services.collection_service import CollectionService
from typing import List
from src.api.v1.deps import get_current_user

collection_router = APIRouter(prefix="/collect")

def get_service(db: Session = Depends(getDatabase)):
    repo = CollectionRepoImpl(db=db)
    return CollectionService(repo=repo)

@collection_router.post("/", response_model= APIResponse[Collection])
def create(colection: Collection, service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    try:
        result = service.create(collection= colection)
        return APIResponse.success_response(result, "Collection created successfully")
    except ValueError as e:
        return APIResponse.error_response(
            message="Failed to create collection",
            error=str(e)
        ) 

@collection_router.get("/", response_model= ListResponse[Collection])
def get_all(param: CollectionParams,service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_all(limit= param.limit, offset= param.offset)
    if not result:
        return ListResponse.create(result, "No collections")
    return ListResponse.create(result, "Collections retrieved successfully")

@collection_router.get("/id", response_model= APIResponse[Collection])
def find_by_id(param: CollectionParams,  service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.find(id= param.id)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a collection",
            error= "Id is null"
        ) 
    return APIResponse.success_response(result, "Collection retrieved successfully")

@collection_router.get("/uui", response_model= ListResponse[Collection])
def find_by_uui(param: CollectionParams,  service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.find_by_uui(uui= param.uui, limit= param.limit, offset= param.offset)
    if not result:
        return ListResponse.create(result, "No collections")
    return ListResponse.create(result, "Collections retrieved successfully")


@collection_router.post("/update", response_model= APIResponse[Collection])
def update(data: UpdateCollection, service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.update(data= data)
    if not result :
        return APIResponse.error_response(
            message="Failed to update",
            error= "Id is null"
        ) 
    return APIResponse.success_response(result, "Collection updated successfully")

@collection_router.get("/latest", response_model= APIResponse[Collection])
def get_timestaps_decs(service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_timestaps_decs()
    if not result :
        return APIResponse.error_response(
            message="Failed to get a collection",
            error= "result is null"
        ) 
    return APIResponse.success_response(result, "Collection retrieved successfully")

@collection_router.get("/timestamp", response_model= APIResponse[TimestampResponse])
def get_latest_timestamp(service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_latest_timestamp()
    result_time = TimestampResponse(timestamp= result)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a collection",
            error= "result is null"
        ) 
    return APIResponse.success_response(result_time, "Collection retrieved successfully")
