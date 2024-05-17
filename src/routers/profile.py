from typing import List

from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import GenericBaseCRUDRouter, get
from fastapi import Depends

from ..db.models.profile import Profile
from ..schemas.profile import ProfileRequestSchema, ProfileSchema, SimplifiedProfileSchema


class ProfileRouter(GenericBaseCRUDRouter[Profile, ProfileSchema, ProfileRequestSchema]):

    @get('/simple', response_model=List[SimplifiedProfileSchema])
    async def get_simple_list(self, dal: CRUDDal = Depends(get_dal_dependency(CRUDDal, model=Profile))) -> List:
        items = dal.list()
        return items

