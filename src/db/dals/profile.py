from common.fastapi.db import CRUDDal

from ..models.profile import Profile


class ProfileDAL(CRUDDal[Profile]):
    ...
