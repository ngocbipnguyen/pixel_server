from src.repositories.photo_repo import IPhotoRepo
from src.schemas.pixel import Photo
from src.models.pixel_model import PhotoModel
from typing import List
from sqlalchemy.orm import Session

class PhotoService():

    def __init__(self, repo: IPhotoRepo):
        self.repo = repo

    
    def create(self, photo: Photo)-> Photo:
        photoModel = PhotoModel(id = photo.id, original= photo.original, large= photo.large,medium= photo.medium,small= photo.small)

        return self.repo.create(photoModel)
    
    def find(self, id: str)-> Photo:
        return self.repo.find(id = id)
    
    def get_photos_id(self)-> List[Photo]:
        return self.repo.get_all()