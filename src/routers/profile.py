from typing import List

from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import GenericBaseCRUDRouter, get, post, put, delete
from common.fastapi.schemas import BasicRequestSchema, HTTPResponseModel, HTTP_200_UPDATED, HTTP_404_DETAIL
from fastapi import Depends, HTTPException

from src.db.dals.auth import oauth2_schema
from ..db.dals.user import UserDAL
from ..db.models.profile import Profile, ProfileFriendship
from ..db.dals.profile import ProfileDAL, ProfileFriendshipDAL
from ..schemas.profile import ProfileRequestSchema, ProfileSchema, SimplifiedProfileSchema


class ProfileRouter(GenericBaseCRUDRouter[Profile, ProfileSchema, ProfileRequestSchema]):

    @get('/simple', response_model=List[SimplifiedProfileSchema])
    async def get_simple_list(self,
                              token: str = Depends(oauth2_schema),
                              dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))) -> List:
        user_dal = dal.get_dal(UserDAL)
        user = user_dal.get_current_user(token)

        items = dal.list(created_by_id=user.id)
        return items

    @post('/create', response_model=ProfileSchema)
    def create(self, request: BasicRequestSchema[ProfileRequestSchema],
               token: str = Depends(oauth2_schema),
               dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):
        user_dal = dal.get_dal(UserDAL)
        friendship_dal = dal.get_dal(ProfileFriendshipDAL)
        user = user_dal.get_current_user(token)
        data = request.data.model_dump()
        result = dal.create(data)
        friendship = friendship_dal.create(
            dict(profile_from_id=user.profile_id, profile_to_id=result.id, safety_correction=0))

        friendship_dal.commit()
        return result

    @post('/free/create', response_model=ProfileSchema)
    async def free_create(self, request: BasicRequestSchema[ProfileRequestSchema],
                          dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):

        data = request.data.model_dump()
        result = dal.create(data)
        return result

    @put('/detail/{profile_id}', response_model=HTTPResponseModel)
    async def update_detail(self, profile_id: int, request: BasicRequestSchema[ProfileRequestSchema],
                            token: str = Depends(oauth2_schema),
                            dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):
        user_dal = dal.get_dal(UserDAL)
        user = user_dal.get_current_user(token)
        desired_profile = dal.get_object_or_404(id=profile_id)

        if desired_profile.created_by_id != user.id:
            return HTTP_404_DETAIL

        data = request.data.model_dump()
        dal.update(data, id=profile_id)
        return HTTP_200_UPDATED

    @delete('/detail/{profile_id}', response_model=HTTPResponseModel)
    async def remove(self, profile_id: int, token: str = Depends(oauth2_schema),
                     dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):
        user_dal = dal.get_dal(UserDAL)
        user = user_dal.get_current_user(token)
        desired_profile = dal.get_object_or_404(id=profile_id)

        if desired_profile.created_by_id != user.id:
            return HTTP_404_DETAIL

        dal.delete(id=profile_id)

        return HTTP_200_UPDATED

    @get('/detail/{profile_id}', response_model=ProfileSchema)
    async def detail(self, profile_id: int, token: str = Depends(oauth2_schema),
                     dal: ProfileDAL = Depends(get_dal_dependency(ProfileDAL))):
        user_dal = dal.get_dal(UserDAL)
        user = user_dal.get_current_user(token)
        desired_profile = dal.get_object_or_404(id=profile_id)

        if not user.profile.friendships.filter(ProfileFriendship.profile_to_id == profile_id).all():
            raise HTTPException(status_code=404)

        return desired_profile
