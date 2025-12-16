from pydantic import BaseModel
from .user import User
class Social(BaseModel):
    id: str
    name: str| None = None
    icon_url: str| None = None
    link: str| None = None

    uui: str

