from pydantic import BaseModel

from src.db.models.wishlist_item import WishlistItem


class WishlistItemSchema(BaseModel):
    name: str
    url: str

    class Config:
        from_attributes = True


class WishlistItemRequestSchema(BaseModel):
    name: str
    url: str
    profile_id: int

    class Config:
        model = WishlistItem
