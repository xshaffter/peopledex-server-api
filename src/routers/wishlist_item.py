from common.fastapi.routing import GenericBaseCRUDRouter

from src.db.models.wishlist_item import WishlistItem
from src.schemas.wishlist_item import WishlistItemSchema, WishlistItemRequestSchema


class WishlistItemRouter(GenericBaseCRUDRouter[WishlistItem, WishlistItemSchema, WishlistItemRequestSchema]):
    ...
