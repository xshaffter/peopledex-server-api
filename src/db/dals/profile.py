from common.fastapi.db import CRUDDal

from ..models.profile import Profile, ProfileFriendship


class ProfileDAL(CRUDDal[Profile]):
    ...


class ProfileFriendshipDAL(CRUDDal[ProfileFriendship]):
    ...
