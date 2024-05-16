from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship


class Profile(Base):
    __schema__ = 'prod'

    created_by_id = Column(Integer, ForeignKey('prod.users.id'))

    name = Column(String)
    birth_date = Column(Date)
    image_url = Column(String)
    vertical_image_url = Column(String)

    # header
    height_cm = Column(Integer)
    weight_kg = Column(Float)
    feet_size = Column(String)
    bottoms_size = Column(String)
    tops_size = Column(String)

    # Basics
    flower = Column(String)
    color = Column(String)
    serie = Column(String)
    music_group = Column(String)
    movie = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    address = Column(String)
    updated_on = Column(TIMESTAMP)

    complexities = relationship("ComplexLike", back_populates="profile")
    wishlist = relationship("WishlistItem", back_populates="profile")
