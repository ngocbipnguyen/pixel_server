from .profile_repo import IProfileRepo
from src.models.user_model import ProfileModel
from typing import Optional
from sqlalchemy.orm import Session
class ProfileRepoImpl(IProfileRepo):

    def __init__(self, db: Session):
        self.db = db

    
    def create(self, profile:ProfileModel)-> ProfileModel:
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile
    
    def find(self, uui: str) -> Optional[ProfileModel]:
        return self.db.query(ProfileModel).filter(ProfileModel.uui == uui).first()