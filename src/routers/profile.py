from common.fastapi.routing import GenericBaseCRUDRouter

from ..db.models.profile import Profile
from ..schemas.profile import ProfileRequestSchema, ProfileSchema


class ProfileRouter(GenericBaseCRUDRouter[Profile, ProfileSchema, ProfileRequestSchema]):
    pass