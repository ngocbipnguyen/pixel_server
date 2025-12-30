from src.repositories.pixel_repo import IPixelRepo
from src.repositories.collection_repo import ICollectionRepo
from src.models.pixel_model import PixelModel, PhotoModel
from src.schemas.collection import UpdateCollection
from src.schemas.pixel import Pixel, map_pixel
from typing import List
import time
from src.schemas.pixel import UpdatePixel
class PixelService():

    def __init__(self, repo: IPixelRepo, repo_coll: ICollectionRepo):
        self.repo = repo
        self.repo_coll = repo_coll


    def create(self, pixel: Pixel) -> Pixel:
        # pixelModel = PixelModel(id = pixel.id, type = pixel.type, width = pixel.width, height = pixel.height,avg_color = pixel.avg_color,collection_id = pixel.collection_id)
        # if pixel.photo:
        #     pixelModel.photo = PhotoModel(
        #         id = pixel.id,
        #         original = pixel.photo.original,
        #         large = pixel.photo.large,
        #         medium = pixel.photo.medium,
        #         small = pixel.photo.small
        #     )
        pixelModel = map_pixel(pixel= pixel, collection_id= pixel.collection_id)
        self.repo_coll.update(UpdateCollection(id= pixel.collection_id,timestamp_update= int(time.time() * 1000)))
        return self.repo.create(pixelModel)
    
    def find(self, id: str)-> Pixel:
        return self.repo.find(id)
    
    def get_pixel_by_collection(self, id)-> List[Pixel]:
        return self.repo.find_by_collection(id)
    
    def get_all(self)-> List[Pixel]:
        return self.repo.get_all()
    
    def updatePixel(self, id: str, data: UpdatePixel):
        return self.repo.update_pixel(id= id, data = data)