from sqlalchemy import Column, String, ForeignKey
from src.database.session import Base
from sqlalchemy.orm import relationship
from uuid import uuid4

class SocialModel(Base):
    __tablename__ = "social"

    id = Column(String, primary_key=True, default= lambda: f"social_{uuid4().hex[:12]}")
    name = Column(String)
    icon_url = Column(String, default= "")
    link = Column(String, default="")

    #FK
    uui = Column(String, ForeignKey("users.uui"), nullable= False)
    user = relationship("UserModel", back_populates="socials")

