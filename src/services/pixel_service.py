from src.repositories.pixel_repo import IPixelRepo
from src.models.pixel_model import PixelModel, PhotoModel
from src.schemas.pixel import Pixel, map_pixel
from typing import List

class PixelService():

    def __init__(self, repo: IPixelRepo):
        self.repo = repo


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
        return self.repo.create(pixelModel)
    
    def find(self, id: str)-> Pixel:
        return self.repo.find(id)
    
    def get_pixel_by_collection(self, id)-> List[Pixel]:
        return self.repo.find_by_collection(id)
    
    def get_all(self)-> List[Pixel]:
        return self.repo.get_all()