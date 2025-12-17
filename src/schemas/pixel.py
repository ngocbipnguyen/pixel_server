from pydantic import BaseModel
from src.models.pixel_model import PixelModel, PhotoModel

class Photo(BaseModel):
    id: str
    original: str
    large: str
    medium: str
    small: str


class Pixel(BaseModel):
    id: str
    type: str
    width: int = 0
    height: int = 0
    avg_color: str
    timestamps: int
    is_favorite: bool = False
    is_mark: bool = False

    collection_id: str
    photo: Photo | None = None


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
