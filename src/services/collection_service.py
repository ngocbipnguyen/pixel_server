from src.repositories.collection_repo import ICollectionRepo
from src.models.collection_model import CollectionModel
from src.models.pixel_model import PixelModel
from src.schemas.collection import Collection, map_collection_to_model, UpdateCollection
from typing import List

class CollectionService():
    def __init__(self, repo: ICollectionRepo):
        self.repo = repo

    def create(self, collection: Collection)-> Collection:
        collectionModel = map_collection_to_model(collection = collection)
        return self.repo.create(collectionModel)
    
    def find(self, id: str)-> Collection:
        return self.repo.find(id)
        
    def find_by_uui(self, uui:str, limit: int, offset: int)-> List[Collection]:
        return self.repo.find_by_uui(uui, limit=limit, offset=offset)
    
    def get_all(self, limit: int, offset: int)-> List[Collection]:
        return self.repo.get_all(limit=limit, offset=offset)
    
    def update(self, data: UpdateCollection): 
        return self.repo.update(data)
    
    def get_timestaps_decs(self):
        return self.repo.get_timestaps_decs()
    
    def get_latest_timestamp(self):
        return self.repo.get_latest_timestamp()
    
    def get_user_by_id(self, id: str):
        return self.repo.get_user_by_id(id)