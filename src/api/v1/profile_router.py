from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.profile_repo import IProfileRepo
from src.repositories.profile_repo_impl import ProfileRepoImpl
from src.schemas.user import Profile
from sqlalchemy.orm import Session
from src.services.profile_service import ProfileService

profile_router = APIRouter(prefix="profile")

def get_server(db: Session = Depends(getDatabase)): 
    repo = ProfileRepoImpl(db=db)
    return ProfileService(repo = repo)

@profile_router.post("/", response_model= Profile)
def create(proflie: Profile, service: ProfileService = Depends(get_server)):
    return service.create(profile= proflie)

@profile_router.get("/uui", response_model=Profile)
def find(uui: str, service: ProfileService = Depends(get_server)):
    return service.find(uui= uui)
