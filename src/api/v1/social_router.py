from fastapi import APIRouter, Depends,HTTPException
from src.database.session import getDatabase
from src.repositories.social_repo_impl import SocialRepoImpl
from src.schemas.social import Social, SocialParams, UpdateSocial
from src.schemas.response import APIResponse, ListResponse
from sqlalchemy.orm import Session
from src.services.social_service import SocialService
from typing import List
from src.api.v1.deps import get_current_user

social_router = APIRouter(prefix="/social")

def get_service(db: Session = Depends(getDatabase)):
    repo = SocialRepoImpl(db= db)
    return SocialService(repo= repo)

@social_router.post("/", response_model= APIResponse[Social])
def create(social: Social, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    try:
        result = service.create(social= social)
        return APIResponse.success_response(result, "Social link created successfully")
    except ValueError as e:
        return APIResponse.error_response(
            message="Failed to create Social",
            error=str(e)
        ) 

@social_router.get("/id", response_model= APIResponse[Social])
def find_by_id(params: SocialParams, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    if not params.id:
        raise HTTPException(status_code=400, detail="UUI is required")
    result = service.find(id= params.id)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a Social by id",
            error= "result is null"
        )  
    return APIResponse.success_response(result, "Social link retrieved successfully")

@social_router.get("/uui", response_model= ListResponse[Social])
def find_by_uui(params: SocialParams, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    if not params.uui:
        raise HTTPException(status_code=400, detail="UUI is required")
    result = service.find_by_uui(uui= params.uui)    
    if not result: 
        return ListResponse.create([], f"No social links found for UUI {params.uui}")
    return ListResponse.create(result, "Social links retrieved successfully")

@social_router.post("/update", response_model= APIResponse[Social])
def find_by_uui(params: UpdateSocial, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.update(data= params)
    if not result :
        return APIResponse.error_response(
            message="Failed to update a Social by id",
            error= "result is null"
        ) 
    return APIResponse.success_response(result, "Social link updated successfully")