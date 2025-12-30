from typing import Optional, Protocol, List
from .pixel_repo import IPixelRepo
from src.models.pixel_model import PixelModel
from sqlalchemy.orm import Session
from src.schemas.pixel import UpdatePixel

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
    
    def update_pixel(self, id: str, data: UpdatePixel)-> Optional[PixelModel]:
        pixel_db = self.db.query(PixelModel).filter(PixelModel.id == id).first()
        if not pixel_db: 
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(pixel_db, key, value)
        
        self.db.commit()
        self.db.refresh(pixel_db)
        return pixel_db