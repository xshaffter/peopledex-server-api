from common.fastapi.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


class Token(Base):
    __schema__ = "prod"
    __tablename__ = "auth_tokens"
    user_id = Column(Integer, ForeignKey('prod.users.id'), unique=True)
    token = Column(String)