from pydantic import BaseModel
from typing import List
from .pixel import Pixel, map_pixel
from src.models.collection_model import CollectionModel
from src.models.pixel_model import PixelModel

class Collection(BaseModel):
    id: str | None = None
    title: str
    description: str | None = None
    is_private: bool | None = None
    media_count: int | None = None
    videos_count: int | None = None
    photos_count: int | None = None
    timestamp_create: int | None = None
    timestamp_update: int | None = None
    uui: str
    pixels: List[Pixel] | None = None

class CollectionParams(BaseModel):
    id: str | None = None
    uui: str | None = None

def map_collection_to_model(collection: Collection) -> CollectionModel:
    db_collection = CollectionModel(
        id=collection.id,
        title=collection.title,
        description=collection.description,
        is_private=collection.is_private,
        media_count=collection.media_count,
        videos_count=collection.videos_count,
        photos_count=collection.photos_count,
        timestamp_create=collection.timestamp_create,
        timestamp_update=collection.timestamp_update,
        uui=collection.uui
    )

    # map pixels nếu có
    if collection.pixels:
        db_collection.pixels = [
            map_pixel(p, collection.id)
            for p in collection.pixels
        ]

    return db_collection
