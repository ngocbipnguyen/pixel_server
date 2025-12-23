from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.profile_repo import IProfileRepo
from src.repositories.profile_repo_impl import ProfileRepoImpl
from src.schemas.user import Profile, ProfileParams
from sqlalchemy.orm import Session
from src.services.profile_service import ProfileService
from src.api.v1.deps import get_current_user


profile_router = APIRouter(prefix="/profile")

def get_server(db: Session = Depends(getDatabase)): 
    repo = ProfileRepoImpl(db=db)
    return ProfileService(repo = repo)

@profile_router.post("/", response_model= Profile)
def create(proflie: Profile, service: ProfileService = Depends(get_server), user_current: str = Depends(get_current_user)):
    return service.create(profile= proflie)

@profile_router.get("/uui", response_model=Profile)
def find(params: ProfileParams, service: ProfileService = Depends(get_server), user_current: str = Depends(get_current_user)):
    return service.find(uui= params.uui)
