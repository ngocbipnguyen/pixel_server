from .collection_repo import ICollectionRepo
from sqlalchemy.orm import Session
from src.models.collection_model import CollectionModel
from typing import Optional, List
from src.schemas.collection import UpdateCollection

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
        return self.db.query(CollectionModel).filter(CollectionModel.uui == uui).order_by(CollectionModel.timestamp_update.desc())
    
    def get_all(self)-> Optional[List[CollectionModel]]:
        return self.db.query(CollectionModel).order_by(CollectionModel.timestamp_update.desc()).all()
    
    def update(self, data: UpdateCollection) -> Optional[CollectionModel]:
        collectionModel = self.db.query(CollectionModel).filter(CollectionModel.id == data.id).first()
        if not collectionModel:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(collectionModel, key, value)

        self.db.commit()
        self.db.refresh(collectionModel)
        return collectionModel