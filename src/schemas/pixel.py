from pydantic import BaseModel
from src.models.pixel_model import PixelModel, PhotoModel

class Photo(BaseModel):
    id: str | None = None
    original: str
    large: str
    medium: str
    small: str

class PhotoParams(BaseModel):
    id: str

class Pixel(BaseModel):
    id: str | None = None
    type: str | None = None
    width: int | None = None
    height: int | None = None
    avg_color: str | None = None
    timestamps: int | None = None
    is_favorite: bool | None = None
    is_mark: bool | None = None

    collection_id: str
    photo: Photo | None = None

class PixelParams(BaseModel):
    id: str | None = None
    collection_id: str | None = None

def map_pixel(pixel: Pixel, collection_id: str) -> PixelModel:
    db_pixel = PixelModel(
        id=pixel.id,
        type=pixel.type,
        width=pixel.width,
        height=pixel.height,
        avg_color=pixel.avg_color,
        is_favorite=pixel.is_favorite,
        is_mark=pixel.is_mark,
        collection_id=collection_id
    )

    if pixel.photo:
        db_pixel.photo = PhotoModel(
            id=pixel.id,  # PK = FK
            original=pixel.photo.original,
            large=pixel.photo.large,
            medium=pixel.photo.medium,
            small=pixel.photo.small
        )

    return db_pixel
