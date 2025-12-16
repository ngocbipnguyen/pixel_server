from pydantic import BaseModel
from typing import List
from .collection import Collection

class Collection(BaseModel):
    id: str
    title: str
    description: str
    is_private: bool
    media_count: int
    videos_count: int
    photos_count: int
    timestamp_create: int
    timestamp_update: int
    uui: str
    collections: List[Collection] | None = None
