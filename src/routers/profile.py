from typing import List

from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import GenericBaseCRUDRouter, get, post
from common.fastapi.schemas import BasicRequestSchema
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
    async def custom_create(self, request: BasicRequestSchema[ProfileRequestSchema],
                              dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):
        data = request.data.dict()
        profile_id = data.pop('created_by_id')
        profile_owner: Profile = dal.get_object(id=profile_id)
        data['created_by_id'] = profile_owner.created_by_id
        result = dal.create(data)
        return result
