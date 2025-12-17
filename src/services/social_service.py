from src.repositories.social_repo import ISocialRepo
from typing import List
from src.models.social_model import SocialModel
from src.schemas.social import Social, map_social
class SocialService:
    
    def __init__(self, repo: ISocialRepo):
        self.repo = repo

    def create(self, social:Social) -> Social:
        model = SocialModel(id = social.id,name = social.name, icon_url = social.icon_url, link = social.link, uui = social.uui)
        return self.repo.create(model)
    
    def find(self, id: str)-> Social:
        return self.repo.find(id)
    
    def find_by_uui(self, uui: str)-> List[Social]:
        return self.repo.find_by_uui(uui)