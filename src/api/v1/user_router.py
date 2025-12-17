from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.user_repo_impl import UserRepoImpl
from src.schemas.user import User
from sqlalchemy.orm import Session
from src.services.user_service import UserService
from typing import List


user_router = APIRouter(prefix="/user")

def get_service(db: Session = Depends(getDatabase)):
    repo = UserRepoImpl(db= db)
    return UserService(repo= repo)


@user_router.post("/", response_model= User)
def create(social: User, service: UserService = Depends(get_service)):
    return service.create(social= social)



@user_router.get("/uui", response_model= User)
def find_by_uui(uui: str, service: UserService = Depends(get_service)):
    return service.find(uui= uui)

@user_router.get("/", response_model= List[User])
def get_all(service: UserService = Depends(get_service)):
    return service.get_all()