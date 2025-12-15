from src.database.session import Base
from sqlalchemy import String, Integer, BigInteger, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
import time

class CollectionModel(Base):
    __tablename__ = "collection"

    id = Column(String, primary_key= True)
    title = Column(String, nullable= False)
    description = Column(String, default="")
    is_private = Column(Boolean, default=False)
    media_count = Column(Integer, default=0)
    videos_count = Column(Integer, default=0)
    photos_count = Column(Integer, default=0)
    timestamp_create = Column(BigInteger, default=lambda: int(time.time() * 1000))
    timestamp_update = Column(BigInteger, default=lambda: int(time.time() * 1000))

    #FK
    uui = Column(String, ForeignKey("users.uui"))
    user = relationship("UserModel", back_populates="collections")

    pixels = relationship("PixelModel", back_populates="collection", cascade="all, delete")

