from common.fastapi.routing import GenericBaseCRUDRouter

from ..db.models.user import User
from ..schemas.user import UserSchema, UserRequestSchema


class UserRouter(GenericBaseCRUDRouter[User, UserSchema, UserRequestSchema]):
    ...