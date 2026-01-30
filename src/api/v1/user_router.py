from fastapi import APIRouter, Depends, HTTPException
from src.database.session import getDatabase
from src.repositories.user_repo_impl import UserRepoImpl
from src.schemas.user import User, UserParams, TokenResponse, LoginRequest, UpdateUser
from src.schemas.response import APIResponse, ListResponse
from sqlalchemy.orm import Session
from src.services.user_service import UserService
from typing import List
from src.api.v1.deps import get_current_user
from src.core.verify_google_token import verify_google_token
from src.schemas.google_login import GoogleLoginRequest

user_router = APIRouter(prefix="/user")

def get_service(db: Session = Depends(getDatabase)):
    repo = UserRepoImpl(db= db)
    return UserService(repo= repo)


@user_router.post("/", response_model= APIResponse[User])
def create(user: User, service: UserService = Depends(get_service)):
    try:
        result = service.create(user= user)
        return APIResponse.success_response(result, "User created successfully")
    except ValueError as e:
        return APIResponse.error_response(
            message="Failed to create user",
            error=str(e)
        )



@user_router.get("/uui", response_model= APIResponse[User])
def find_by_uui(param: UserParams = Depends(), service: UserService = Depends(get_service), user_current: str = Depends(get_current_user)):
    if not param.uui:
        raise HTTPException(status_code=400, detail="UUI is required")
    result = service.find(uui= param.uui)
    if not result:
        return APIResponse.error_response(
            message="User not found",
            error=f"User with UUI {param.uui} does not exist"
        )
    return APIResponse.success_response(result, "User retrieved successfully")


@user_router.get("/", response_model= ListResponse[User])
def get_all(service: UserService = Depends(get_service), user_current: str = Depends(get_current_user)):
    result = service.get_all()
    if not result: 
        return ListResponse.create([], f"No user")
    return ListResponse.create(result, "Users retrieved successfully")

@user_router.post("/login", response_model= APIResponse[TokenResponse])
def login(request: LoginRequest, service: UserService = Depends(get_service)):
    result = service.login(email= request.email, password= request.password)
    return APIResponse.success_response(result, "Login successful")

@user_router.post("/update", response_model= APIResponse[User])
def update(data: UpdateUser = Depends(), service: UserService = Depends(get_service),  user_current: str = Depends(get_current_user)):
    result = service.update(data=data)
    if not result: 
        return APIResponse.error_response(
            message="User update",
            error=f"User update failure!"
        )
    return APIResponse.success_response(result, "User updated successfully")


@user_router.post("/login/google", response_model= APIResponse[TokenResponse])
def login_google(req: GoogleLoginRequest, service: UserService = Depends(get_service)):
    result = service.login_google(req.id_token)
    return APIResponse.success_response(result, "Login by google successful!")


@user_router.get("/access_tokens", response_model= APIResponse[User])
def find_by_token(param: UserParams = Depends(), service: UserService = Depends(get_service)):
    if not param.token:
        raise HTTPException(status_code=400, detail="Token is required")
    result = service.find_token(token= param.token)
    if not result:
        return APIResponse.error_response(
            message="User not found",
            error=f"User with token {param.token} does not exist"
        )
    return APIResponse.success_response(result, "User retrieved successfully")