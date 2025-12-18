from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.social_repo_impl import SocialRepoImpl
from src.schemas.social import Social, SocialParams
from sqlalchemy.orm import Session
from src.services.social_service import SocialService
from typing import List

social_router = APIRouter(prefix="/social")

def get_service(db: Session = Depends(getDatabase)):
    repo = SocialRepoImpl(db= db)
    return SocialService(repo= repo)

@social_router.post("/", response_model= Social)
def create(social: Social, service: SocialService = Depends(get_service)):
    return service.create(social= social)

@social_router.get("/id", response_model= Social)
def find_by_id(params: SocialParams, service: SocialService = Depends(get_service)):
    return service.find(id= params.id)

@social_router.get("/uui", response_model= List[Social])
def find_by_uui(params: SocialParams, service: SocialService = Depends(get_service)):
    return service.find_by_uui(uui= params.uui)