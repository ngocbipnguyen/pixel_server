from src.repositories.collection_repo import ICollectionRepo
from src.models.collection_model import CollectionModel
from src.models.pixel_model import PixelModel
from src.schemas.collection import Collection, map_collection_to_model
from typing import List

class CollectionService():
    def __init__(self, repo: ICollectionRepo):
        self.repo = repo

    def create(self, collection: Collection)-> Collection:
        collectionModel = map_collection_to_model(collection = collection)
        return self.repo.create(collectionModel)
    
    def find(self, id: str)-> Collection:
        return self.repo.find(id)
        
    def find_by_uui(self, uui:str)-> List[Collection]:
        return self.repo.find_by_uui(uui)
    
    def get_all(self)-> List[Collection]:
        return self.repo.get_all()