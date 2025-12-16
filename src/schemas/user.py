from pydantic import BaseModel
from .social import Social
from .collection import Collection
from typing import List

class Profile(BaseModel):
    uui: str
    total_view: int
    all_time_rank: int
    month_rank: int

class User(BaseModel):
    uui: str
    email: str
    name: str
    url: str| None = None
    token: str| None = None
    timestamps: int
    is_active: bool| None = None
    follow: bool| None = None
    profile: Profile
    socials: List[Social]| None = None
    collections: List[Collection]| None = None

