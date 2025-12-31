from fastapi import FastAPI
from src.api.v1.collection_router import collection_router
from src.api.v1.pixel_router import pixel_router
from src.api.v1.profile_router import profile_router
from src.api.v1.social_router import social_router
from src.api.v1.user_router import user_router
from src.database.session import Base, engine
from src.api.v1.upload import router_upload
app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(collection_router, prefix="/v1")

app.include_router(pixel_router, prefix="/v1")

app.include_router(profile_router, prefix="/v1")

app.include_router(social_router, prefix="/v1")

app.include_router(user_router, prefix="/v1")

app.include_router(router_upload, prefix="/v1")