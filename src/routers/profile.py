from typing import List

from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import GenericBaseCRUDRouter, get, post
from fastapi import Depends

from ..db.models.profile import Profile
from ..db.dals.profile import ProfileDAL
from ..schemas.profile import ProfileRequestSchema, ProfileSchema, SimplifiedProfileSchema


class ProfileRouter(GenericBaseCRUDRouter[Profile, ProfileSchema, ProfileRequestSchema]):

    @get('/simple', response_model=List[SimplifiedProfileSchema])
    async def get_simple_list(self, dal: CRUDDal = Depends(get_dal_dependency(CRUDDal, model=Profile))) -> List:
        items = dal.list()
        return items

    @post('/custom/create', response_model=ProfileSchema)
    async def custom_create(self, request: ProfileRequestSchema,
                              dal: CRUDDal = Depends(get_dal_dependency(ProfileDAL))):
        data = request.data
        result = dal.create(data)
        return result
