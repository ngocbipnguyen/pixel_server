from src.database.session import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
import time

class PixelModel(Base):
    __tablename__ = "pixel"

    id = Column(String, primary_key=True)
    type = Column(String)
    # url
    width = Column(Integer, default=0)
    height = Column(Integer, default=0)
    avg_color = Column(String, default="")
    timestamps = Column(BigInteger,default=lambda: int(time.time() * 1000))
    is_favorite = Column(Boolean, default= False)
    is_mark = Column(Boolean, default= False)
    
    #FK
    collection_id = Column(String, ForeignKey("collection.id"))
    collection = relationship("CollectionModel", back_populates="pixels")

    photo = relationship("PhotoModel", back_populates="pixel", cascade="all, delete")


class PhotoModel(Base):
    __tablename__ = "photo"

    id = Column(String, ForeignKey("pixel.id"), primary_key=True)
    original = Column(String, nullable=False)
    large = Column(String, nullable=False)
    medium = Column(String, nullable=False)
    small = Column(String, nullable=False)

    pixel = relationship("PixelModel", back_populates="photo")


