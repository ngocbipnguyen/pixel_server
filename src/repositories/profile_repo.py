from typing import Protocol, Optional, List
from src.models.user_model import ProfileModel

class IProfileRepo(Protocol):
    
    def create(profile: ProfileModel)-> ProfileModel:...

    def find(uui: str)-> Optional[ProfileModel]:...