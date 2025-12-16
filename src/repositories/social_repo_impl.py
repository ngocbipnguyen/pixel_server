from .social_repo import ISocialRepo
from sqlalchemy.orm import Session
from src.models.social_model import SocialModel
from typing import Optional, List
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
    
    
    
    