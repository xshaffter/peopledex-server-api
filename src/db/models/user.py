from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey


class User(Base):
    __schema__ = 'prod'

    username = Column(String)
    profile_id = Column(Integer, ForeignKey('prod.profiles.id'), unique=True)
    password_hash = Column(String)
