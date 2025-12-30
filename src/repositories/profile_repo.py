from typing import Protocol, Optional, List
from src.models.user_model import ProfileModel
from src.schemas.user import UpdateProfile
class IProfileRepo(Protocol):
    
    def create(profile: ProfileModel)-> ProfileModel:...

    def find(uui: str)-> Optional[ProfileModel]:...
    
    def update(data: UpdateProfile)-> Optional[ProfileModel]:...