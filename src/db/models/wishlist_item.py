from common.fastapi.db import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column


class WishlistItem(Base):
    __schema__ = 'prod'

    name = Column(String)
    profile_id = mapped_column(ForeignKey('prod.profiles.id'))
    url = Column(String)
    profile = relationship("Profile", back_populates="wishlist")
