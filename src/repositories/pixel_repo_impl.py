from typing import Optional, Protocol, List
from .pixel_repo import IPixelRepo
from src.models.pixel_model import PixelModel
from sqlalchemy.orm import Session

class PixelRepoImpl(IPixelRepo):

    def __init__(self, db: Session):
        self.db = db

    
    def create(self, pixel: PixelModel) -> PixelModel:
        self.db.add(pixel)
        self.db.commit()
        self.db.refresh(pixel)
        return pixel
    
    def find(self, id:str) -> Optional[PixelModel]:
        return self.db.query(PixelModel).filter(PixelModel.id == id).first()
    
    def find_by_collection(self,id:str) -> Optional[List[PixelModel]]:
        return self.db.query(PixelModel).filter(PixelModel.collection_id == id)
    
    def get_all(self)-> Optional[List[PixelModel]]:
        return self.db.query(PixelModel).all()