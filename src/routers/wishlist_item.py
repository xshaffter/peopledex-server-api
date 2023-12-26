from common.fastapi.routing import GenericBaseCRUDRouter

from src.db.models.wishlist_item import WishlistItem
from src.schemas.wishlist_item import WishlistItemSchema, WishlistItemRequestSchema


class ComplexLikeRouter(GenericBaseCRUDRouter[WishlistItem, WishlistItemSchema, WishlistItemRequestSchema]):
    ...
