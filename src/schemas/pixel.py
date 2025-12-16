from pydantic import BaseModel

class Photo(BaseModel):
    id: str
    original: str
    large: str
    medium: str
    small: str


class Pixel(BaseModel):
    id: str
    type: str
    width: int
    height: int
    avg_color: str
    timestamps: int
    is_favorite: bool
    is_mark: bool

    collection_id: str
    photo: Photo | None = None