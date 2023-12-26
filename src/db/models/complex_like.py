from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column


class ComplexLike(Base):
    __schema__ = 'prod'

    name = Column(String)
    profile_id = mapped_column(ForeignKey('prod.profiles.id'))
    favorite = Column(String)
    profile = relationship("Profile", back_populates="complexities")
