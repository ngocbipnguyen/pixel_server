from .social_repo import ISocialRepo
from sqlalchemy.orm import Session
from src.models.social_model import SocialModel
from typing import Optional, List
from src.schemas.social import UpdateSocial


class SocialRepoImpl(ISocialRepo):

    def __init__(self, db: Session):
        self.db = db

    def create(self,social: SocialModel)-> SocialModel:
        self.db.add(social)
        self.db.commit()
        self.db.refresh(social)
        return social
    
    def find(self, id: str) -> Optional[SocialModel]:
        return self.db.query(SocialModel).filter(SocialModel.id == id).first()
    
    def find_by_uui(self, uui: str) -> Optional[List[SocialModel]]:
        return self.db.query(SocialModel).filter(SocialModel.uui == uui)
    
    def update(self, update: UpdateSocial) -> Optional[SocialModel]:
        social_model = self.db.query(SocialModel).filter(SocialModel.id == update.id).first()
        if not social_model:
            return None
        for key, value in update.model_dump(exclude_unset=True).items():
            setattr(social_model, key, value)
        
        self.db.commit()
        self.db.refresh(social_model)
        return social_model
    
    
    
    