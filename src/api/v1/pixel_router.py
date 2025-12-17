from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.pixel_repo_impl import PixelRepoImpl
from src.schemas.pixel import Pixel
from sqlalchemy.orm import Session
from src.services.pixel_service import PixelService
from typing import List
pixel_router = APIRouter(prefix="pixel")

def get_service(db: Session = Depends(getDatabase)):
    repo = PixelRepoImpl(db= db)
    return PixelService(repo= repo)

@pixel_router.post("/", response_model= Pixel)
def create(pixel: Pixel, service: PixelService = Depends(get_service)):
    return service.create(pixel=pixel)

@pixel_router.get("/id", response_model=Pixel)
def find_by_id(id: str, service: PixelService = Depends(get_service)):
    return service.find(id= id)

@pixel_router.get("/id_collect", response_model= List[Pixel])
def find_by_collect(idc: str, service: PixelService = Depends(get_service)):
    return service.get_pixel_by_collection(id= idc)

@pixel_router.get("/", response_model=List[Pixel])
def get_all(service: PixelService = Depends(get_service)):
    return service.get_all()