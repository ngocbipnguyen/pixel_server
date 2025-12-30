from src.repositories.profile_repo import IProfileRepo
from src.schemas.user import Profile, UpdateProfile
from src.models.user_model import ProfileModel
class ProfileService:

    def __init__(self, repo: IProfileRepo):
        self.repo = repo

    
    def create(self, profile: Profile)-> Profile:
        profileModel = ProfileModel(uui = profile.uui, 
                                    total_view = profile.total_view, 
                                    all_time_rank = profile.all_time_rank,
                                    month_rank = profile.month_rank)
        
        return self.repo.create(profileModel)
        
    def find(self, uui: str)-> Profile:
        return self.repo.find(uui = uui)
    
    def update(self, data: UpdateProfile):
        return self.repo.update(data)