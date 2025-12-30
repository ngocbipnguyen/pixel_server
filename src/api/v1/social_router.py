from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.social_repo_impl import SocialRepoImpl
from src.schemas.social import Social, SocialParams, UpdateSocial
from sqlalchemy.orm import Session
from src.services.social_service import SocialService
from typing import List
from src.api.v1.deps import get_current_user

social_router = APIRouter(prefix="/social")

def get_service(db: Session = Depends(getDatabase)):
    repo = SocialRepoImpl(db= db)
    return SocialService(repo= repo)

@social_router.post("/", response_model= Social)
def create(social: Social, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.create(social= social)

@social_router.get("/id", response_model= Social)
def find_by_id(params: SocialParams, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find(id= params.id)

@social_router.get("/uui", response_model= List[Social])
def find_by_uui(params: SocialParams, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find_by_uui(uui= params.uui)

@social_router.post("/update", response_model = Social)
def find_by_uui(params: UpdateSocial, service: SocialService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.update(data= params)