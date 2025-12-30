from fastapi import APIRouter, Depends
from src.database.session import getDatabase
from src.repositories.collection_repo_impl import CollectionRepoImpl
from src.schemas.collection import Collection, CollectionParams, UpdateCollection
from sqlalchemy.orm import Session
from src.services.collection_service import CollectionService
from typing import List
from src.api.v1.deps import get_current_user

collection_router = APIRouter(prefix="/collect")

def get_service(db: Session = Depends(getDatabase)):
    repo = CollectionRepoImpl(db=db)
    return CollectionService(repo=repo)

@collection_router.post("/", response_model=Collection)
def create(colection: Collection, service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.create(collection= colection)

@collection_router.get("/", response_model= List[Collection])
def get_all(service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.get_all()

@collection_router.get("/id", response_model= Collection)
def find_by_id(param: CollectionParams,  service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find(id= param.id)

@collection_router.get("/uui", response_model= List[Collection])
def find_by_uui(param: CollectionParams,  service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.find_by_uui(uui= param.uui)


@collection_router.post("/update", response_model= Collection)
def update(data: UpdateCollection, service: CollectionService = Depends(get_service), user_current: str = Depends(get_current_user)):
    return service.update(data= data)
