from pydantic import BaseModel
from .user import User
from src.models.social_model import SocialModel

class Social(BaseModel):
    id: str
    name: str| None = None
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
