from common.fastapi.db import Base
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship


class ProfileFriendship(Base):
    __schema__ = 'prod'

    profile_from_id = Column(Integer, ForeignKey('prod.profiles.id'))
    profile_to_id = Column(Integer, ForeignKey('prod.profiles.id'))
    safety_correction = Column(Integer)
    profile_from = relationship("Profile", back_populates="friendships", foreign_keys=[profile_from_id], uselist=True,
                                viewonly=True)
    profile_to = relationship("Profile", uselist=False, viewonly=True, foreign_keys=[profile_to_id])


class Profile(Base):
    __schema__ = 'prod'

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
    friendships = relationship("ProfileFriendship", back_populates="profile_from", lazy='dynamic',
                               foreign_keys=[ProfileFriendship.profile_from_id])
