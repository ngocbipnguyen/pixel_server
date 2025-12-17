from src.repositories.user_repo import IUserRepo
from typing import List
from src.models.user_model import UserModel, ProfileModel
from src.models.collection_model import CollectionModel
from src.models.social_model import SocialModel
from src.schemas.user import User

class UserService:

    def __init__(self, repo: IUserRepo):
        self.repo = repo

    def create(self, user: User)-> User:
        
        userModel = UserModel(uui = user.uui, 
                              email = user.email, 
                              name = user.name,
                              url = user.url, 
                              token =user.token,
                              is_active = user.is_active,
                              follow = user.follow
                              )
        
        return self.repo.create(userModel)
    
    def find(self, uui: str)-> User:
        return self.repo.find(uui=uui)
    
    def get_all(self)-> List[User]:
        return self.repo.get_all()