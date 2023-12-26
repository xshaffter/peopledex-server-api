from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float


class User(Base):
    __schema__ = 'prod'

    username = Column(String)
    profile_id = Column(Integer)
    password_hash = Column(String)
