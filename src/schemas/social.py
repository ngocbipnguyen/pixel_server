from pydantic import BaseModel
from src.models.social_model import SocialModel
from typing import Optional
class Social(BaseModel):
    id: str| None = None
    name: str
    icon_url: str| None = None
    link: str| None = None

    uui: str


def map_social(social: Social)-> SocialModel:
    model = SocialModel(id = social.id,
                        name = social.name, 
                        icon_url = social.icon_url, 
                        link = social.link, 
                        uui = social.uui)
    return model


class SocialParams(BaseModel):
    id: str | None = None
    uui: str | None = None


class UpdateSocial(BaseModel):
    id: str | None = None 
    name: Optional[str] = None
    icon_url: Optional[str] = None
    link: Optional[str] = None