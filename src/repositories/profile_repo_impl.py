from .profile_repo import IProfileRepo
from src.models.user_model import ProfileModel
from typing import Optional
from sqlalchemy.orm import Session
from src.schemas.user import UpdateProfile

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
    
    def update(self, data: UpdateProfile) -> Optional[ProfileModel]:
        profile = self.db.query(ProfileModel).filter(ProfileModel.uui == data.uui).first()
        
        for key, value in data.model_dump(exclude_unset= True).items():
            setattr(profile, key, value)

        self.db.commit()
        self.db.refresh(profile)

        return profile