from pydantic import BaseModel

from src.db.models.wishlist_item import WishlistItem


class WishlistItemSchema(BaseModel):
    name: str
    favorite: str

    class Config:
        from_attributes = True


class WishlistItemRequestSchema(BaseModel):
    name: str
    favorite: str
    profile_id: int

    class Config:
        model = WishlistItem
