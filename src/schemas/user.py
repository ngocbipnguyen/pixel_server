from pydantic import BaseModel
from .social import Social, map_social
from .collection import Collection, map_collection_to_model
from typing import List
from src.models.user_model import ProfileModel, UserModel

class Profile(BaseModel):
    uui: str
    total_view: int | None = None
    all_time_rank: int | None = None
    month_rank: int | None = None

class User(BaseModel):
    uui: str | None = None
    email: str
    name: str
    url: str| None = None
    token: str| None = None
    timestamps: int | None = None
    is_active: bool| None = None
    follow: bool| None = None
    profile: Profile | None = None
    socials: List[Social]| None = None
    collections: List[Collection]| None = None


class UserParams(BaseModel):
    uui: str | None = None
    email: str | None = None

class ProfileParams(BaseModel):
    uui: str

def map_profile(profile: Profile)-> ProfileModel:
    profileModel = profileModel(uui = profile.uui, 
                                total_view = profile.total_view, 
                                all_time_rank = profile.all_time_rank,
                                month_rank = profile.month_rank)
    return profileModel

def map_user(user: User)-> UserModel:
    userModel = UserModel(uui = user.uui, 
                            email = user.email, 
                            name = user.name,
                            url = user.url, 
                            token =user.token,
                            is_active = user.is_active,
                            follow = user.follow
                            )
    if user.socials:
        userModel.socials = [
            map_social(social)
            for social in user.socials
        ]
    
    if user.profile:
        userModel.profile = map_profile(user.profile)

    if user.collections:
        userModel.collections = [
            map_collection_to_model(collection)
            for collection in user.collections
        ]

    return userModel


