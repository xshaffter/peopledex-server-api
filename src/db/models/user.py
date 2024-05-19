from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __schema__ = 'prod'

    username = Column(String)
    profile_id = Column(Integer, ForeignKey('prod.profiles.id'), unique=True)
    password_hash = Column(String)
    profile = relationship("Profile")
