from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float
from sqlalchemy.orm import relationship


class Profile(Base):
    __schema__ = 'prod'

    name = Column(String)
    height_cm = Column(Integer)
    weight_kg = Column(Float)
    birth_date = Column(Date)
    image_url = Column(String)
    vertical_image_url = Column(String)
    feet = Column(Integer)
    bottoms = Column(Integer)
    tops = Column(Integer)

    complexities = relationship("ComplexLike", back_populates="profile")