from .collection_repo import ICollectionRepo
from sqlalchemy.orm import Session
from src.models.collection_model import CollectionModel
from typing import Optional, List

class CollectionRepoImpl(ICollectionRepo):

    def __init__(self, db: Session):
        self.db = db
    
    def create(self, collection: CollectionModel) -> CollectionModel:
        self.db.add(collection)
        self.db.commit()
        self.db.refresh(collection)
        return collection
    
    def find(self,id: str)-> Optional[CollectionModel]:
        return self.db.query(CollectionModel).filter(CollectionModel.id == id).first()
    
    def find_by_uui(self,uui: str)-> Optional[List[CollectionModel]]:
        return self.db.query(CollectionModel).filter(CollectionModel.uui == uui)
    
    def get_all(self)-> Optional[List[CollectionModel]]:
        return self.db.query(CollectionModel).all()