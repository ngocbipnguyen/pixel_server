from src.repositories.user_repo import IUserRepo
from typing import List
from src.models.user_model import UserModel, ProfileModel
from src.models.collection_model import CollectionModel
from src.models.social_model import SocialModel
from src.schemas.user import User, map_user, TokenResponse, verify_password, TokenResponse, UpdateUser
from fastapi import HTTPException
from src.core.config import create_refresh_token, create_token

class UserService:

    def __init__(self, repo: IUserRepo):
        self.repo = repo

    def create(self, user: User)-> User:
        
        userModel = map_user(user= user)
        
        return self.repo.create(userModel)
    
    def find(self, uui: str)-> User:
        return self.repo.find(uui=uui)
    
    def get_all(self)-> List[User]:
        return self.repo.get_all()
    
    def login(self, email, password)-> TokenResponse:
        user = self.repo.find_email(email = email)
        if not user: 
            raise HTTPException(status_code=401, detail="")
        
        if not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="password was wrong!")

        access_token = create_token(data= {"sub": user.uui})
        refresh_token = create_refresh_token(user.uui)
        return TokenResponse(access_token= access_token, refresh_token= refresh_token)
    
    def update(self, data: UpdateUser): 
        return self.repo.update(data)

