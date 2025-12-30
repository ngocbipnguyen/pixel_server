from .user_repo import IUserRepo
from src.models.user_model import UserModel
from sqlalchemy.orm import Session
from typing import Optional, List
from src.schemas.user import UpdateUser

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
    
    def find_email(self,email: str)-> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def login(self, email: str, password: str)-> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def update(self, data: UpdateUser)-> Optional[UserModel]:
        user = self.db.query(UserModel).filter(UserModel.uui == data.uui).first()
        for key, value in data.model_dump(exclude_unset= True).items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user