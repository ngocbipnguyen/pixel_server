from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.user_repo_impl import UserRepoImpl
from src.schemas.user import User, UserParams, TokenResponse, LoginRequest, UpdateUser
from sqlalchemy.orm import Session
from src.services.user_service import UserService
from typing import List
from src.api.v1.deps import get_current_user

user_router = APIRouter(prefix="/user")

def get_service(db: Session = Depends(getDatabase)):
    repo = UserRepoImpl(db= db)
    return UserService(repo= repo)


@user_router.post("/", response_model= User)
def create(user: User, service: UserService = Depends(get_service)):
    return service.create(user= user)



@user_router.get("/uui", response_model= User)
def find_by_uui(param: UserParams, service: UserService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find(uui= param.uui)

@user_router.get("/", response_model= List[User])
def get_all(service: UserService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.get_all()

@user_router.post("/login", response_model= TokenResponse)
def login(request: LoginRequest, service: UserService = Depends(get_service)):
    return service.login(email= request.email, password= request.password)

@user_router.post("/update", response_model=User)
def update(data: UpdateUser, service: UserService = Depends(get_service),  user_current: str = Depends(get_current_user)):
    return service.update(data=data)