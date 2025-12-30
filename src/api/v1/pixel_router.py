from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.pixel_repo_impl import PixelRepoImpl
from src.schemas.pixel import Pixel, PixelParams, UpdatePixel
from sqlalchemy.orm import Session
from src.services.pixel_service import PixelService
from src.repositories.collection_repo_impl import CollectionRepoImpl
from typing import List
from src.api.v1.deps import get_current_user

pixel_router = APIRouter(prefix="/pixel")

def get_service(db: Session = Depends(getDatabase)):
    repo = PixelRepoImpl(db= db)
    repo_coll = CollectionRepoImpl(db=db)
    return PixelService(repo= repo, repo_coll= repo_coll)

@pixel_router.post("/", response_model= Pixel)
def create(pixel: Pixel, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.create(pixel=pixel)

@pixel_router.get("/id", response_model=Pixel)
def find_by_id(param: PixelParams, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find(id= param.id)

@pixel_router.get("/id_collect", response_model= List[Pixel])
def find_by_collect(param: PixelParams, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.get_pixel_by_collection(id= param.collection_id)

@pixel_router.get("/", response_model=List[Pixel])
def get_all(service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.get_all()

@pixel_router.post("/update", response_model= Pixel)
def update_pixel(update: UpdatePixel, service: PixelService = Depends(get_service), user_current: str = Depends(get_current_user)): 
    return service.updatePixel(id= update.id, data= update)