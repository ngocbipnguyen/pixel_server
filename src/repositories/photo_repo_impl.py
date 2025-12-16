from .photo_repo import IPhotoRepo
from sqlalchemy.orm import Session
from src.models.pixel_model import PhotoModel
from typing import Optional, List

class PhotoRepoImpl(IPhotoRepo):

    def __init__(self, db:Session):
        self.db = db

    def create(self,photo: PhotoModel)-> PhotoModel:
        self.db.add(photo)
        self.db.commit()
        self.db.refresh(photo)
        return photo
    
    def find(self, id: str)-> Optional[PhotoModel]:
        return self.db.query(PhotoModel).filter(PhotoModel.id == id).first()
    
    def get_all(self)-> Optional[List[PhotoModel]]:
        return self.db.query(PhotoModel).all()
    