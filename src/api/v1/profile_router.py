from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.profile_repo import IProfileRepo
from src.repositories.profile_repo_impl import ProfileRepoImpl
from src.schemas.user import Profile, ProfileParams, UpdateProfile
from src.schemas.response import APIResponse
from sqlalchemy.orm import Session
from src.services.profile_service import ProfileService
from src.api.v1.deps import get_current_user


profile_router = APIRouter(prefix="/profile")

def get_server(db: Session = Depends(getDatabase)): 
    repo = ProfileRepoImpl(db=db)
    return ProfileService(repo = repo)

@profile_router.post("/", response_model= APIResponse[Profile])
def create(proflie: Profile, service: ProfileService = Depends(get_server), user_current: str = Depends(get_current_user)):
    try: 
        result = service.create(profile= proflie)
        return APIResponse.success_response(result, "Profile created successfully")
    except ValueError as e:
        return APIResponse.error_response(
            message="Failed to create Profile",
            error=str(e)
        ) 

@profile_router.get("/uui", response_model= APIResponse[Profile])
def find(params: ProfileParams = Depends(), service: ProfileService = Depends(get_server), user_current: str = Depends(get_current_user)):
    result = service.find(uui= params.uui)
    if not result :
        return APIResponse.error_response(
            message="Failed to get a profile",
            error= "result is null"
        ) 
    return APIResponse.success_response(result, "Profile retrieved successfully")


@profile_router.post("/update", response_model= APIResponse[Profile])
def update(params: UpdateProfile,  service: ProfileService = Depends(get_server), user_current: str = Depends(get_current_user)):
    result = service.update(params)
    if not result: 
        return APIResponse.error_response(
            message="Pixel update",
            error=f"Pixel update failure!"
        )
    return APIResponse.success_response(result, "Profile updated successfully")