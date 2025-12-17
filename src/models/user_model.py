from sqlalchemy import Column, String, BigInteger, ForeignKey, Boolean
from src.database.session import Base
from uuid import uuid4
from sqlalchemy.orm import relationship
import time

class UserModel(Base):
    __tablename__ =  "users"

    uui = Column(String, primary_key=True, default=lambda:str(uuid4()))
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable= False)
    url = Column(String)
    token = Column(String)
    timestamps = Column(BigInteger,default=lambda: int(time.time() * 1000))
    is_active = Column(Boolean, default= False)
    follow = Column(Boolean, default=False)
    #FK
    profile = relationship("ProfileModel", 
                           back_populates="user",
                           uselist=False,
                           cascade="all, delete")
    socials = relationship("SocialModel",
                           back_populates="user",
                           cascade="all, delete-orphan")
    collections = relationship("Collection_model", back_populates="user",cascade="all, delete-orphan")




class ProfileModel(Base):
    __tablename = "profile"

    uui = Column(String, ForeignKey("users.uui"), primary_key=True)
    total_view = Column(BigInteger, default=0)
    all_time_rank = Column(BigInteger, default=0)
    month_rank = Column(BigInteger, default=0)
    
    # FK
    user = relationship("UserModel", back_populates="profile")
