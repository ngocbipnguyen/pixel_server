from .user_repo import IUserRepo
from src.models.user_model import UserModel
from sqlalchemy.orm import Session
from typing import Optional, List
class UserRepoImpl(IUserRepo):

    def __init__(self, db: Session):
        self.db = db

    def create(self,user: UserModel)-> UserModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def find(self, uui: str)-> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.uui == uui).first()
    
    def get_all(self)-> Optional[List[UserModel]]:
        return self.db.query(UserModel).all()