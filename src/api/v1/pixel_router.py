from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.pixel_repo_impl import PixelRepoImpl
from src.schemas.pixel import Pixel, PixelParams, UpdatePixel, TimestampResponse
from src.schemas.response import APIResponse, ListResponse
from sqlalchemy.orm import Session
from src.services.pixel_service import PixelService
from src.repositories.collection_repo_impl import CollectionRepoImpl
from typing import List
from src.api.v1.deps import get_current_user

pixel_router = APIRouter(prefix="/pixel")

def get_service(db: Session = Depends(getDatabase)):
    repo = PixelRepoImpl(db= db)
    repo_coll = CollectionRepoImpl(db=db)
    return PixelService(repo= repo, repo_coll= repo_coll)

@pixel_router.post("/", response_model= APIResponse[Pixel])
def create(pixel: Pixel, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    try:
        result = service.create(pixel=pixel)
        return APIResponse.success_response(result, "Pixel created successfully")
    except ValueError as e:
        return APIResponse.error_response(
            message="Failed to create Pixel",
            error=str(e)
        ) 

@pixel_router.get("/id", response_model= APIResponse[Pixel])
def find_by_id(param: PixelParams, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.find(id= param.id)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a pixel",
            error= "result is null"
        ) 
    return APIResponse.success_response(result, "Pixel retrieved successfully")

@pixel_router.get("/id_collect", response_model= ListResponse[Pixel])
def find_by_collect(param: PixelParams, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_pixel_by_collection(id= param.collection_id, limit= param.limit, offset= param.offset)
    if not result:
        return ListResponse.create(result, "No pixel")
    return ListResponse.create(result, "Pixels retrieved successfully")

@pixel_router.get("/", response_model= ListResponse[Pixel])
def get_all(param: PixelParams, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_all(limit= param.limit, offset= param.offset)
    if not result:
        return ListResponse.create(result, "No pixel")
    return ListResponse.create(result, "Pixels retrieved successfully")

@pixel_router.post("/update", response_model= APIResponse[Pixel])
def update_pixel(update: UpdatePixel, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)): 
    result = service.updatePixel(id= update.id, data= update)
    if not result: 
        return APIResponse.error_response(
            message="Pixel update",
            error=f"Pixel update failure!"
        )
    return APIResponse.success_response(result, "Pixel updated successfully")

@pixel_router.get("/latest", response_model= APIResponse[Pixel])
def get_timestaps_decs(service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_timestaps_decs()
    if not result :
        return APIResponse.error_response(
            message="Failed to get a pixel",
            error= "result is null"
        ) 
    return APIResponse.success_response(result, "Pixel retrieved successfully")

@pixel_router.get("/timestamp", response_model= APIResponse[Pixel])
def get_latest_timestamp(service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_latest_timestamp()
    result_time = TimestampResponse(timestamp= result)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a pixel",
            error= "result is null"
        ) 
    return APIResponse.success_response(result_time, "Pixel retrieved successfully")