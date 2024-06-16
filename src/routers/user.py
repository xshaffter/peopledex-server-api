from typing import List

from common.fastapi.db import get_dal_dependency, CRUDDal
from common.fastapi.routing import GenericBaseRouter, post, get
from common.fastapi.schemas import BasicRequestSchema, HTTP_201_CREATED, HTTPResponseModel
from fastapi import Depends
from fastapi_pagination import Page, paginate
from sqlmodel import select, any_

from src.db.dals.auth import oauth2_schema
from src.db.dals.profile import ProfileDAL
from src.db.dals.user import UserDAL
from src.db.models.profile import Profile
from src.db.models.user import User
from src.schemas.profile import ProfileSchema, SimplifiedProfileSchema
from src.schemas.user import UserRegisterData


class UserRouter(GenericBaseRouter[User]):

    @post('/register', response_model=HTTPResponseModel)
    def register(self, request: BasicRequestSchema[UserRegisterData],
                 dal: UserDAL = Depends(get_dal_dependency(UserDAL))):
        dal.create(request.data)
        return HTTP_201_CREATED

    @get("/friends", response_model=Page[SimplifiedProfileSchema])
    def get_friends(self, query = "", token: str = Depends(oauth2_schema), dal: UserDAL = Depends(get_dal_dependency(UserDAL))):
        user = dal.get_current_user(token)
        user_profile: Profile = user.profile
        result = [friendship.profile_to for friendship in user_profile.friendships]
        filtered_items = filter(lambda item: query.lower() in item.name.lower(), result)
        items = sorted(filtered_items, key=Profile.__sort__)
        return paginate(items)

    @get("/profile", response_model=ProfileSchema)
    def get_profile(self, token: str = Depends(oauth2_schema), dal: UserDAL = Depends(get_dal_dependency(UserDAL))):
        user = dal.get_current_user(token)
        profile_dal: ProfileDAL = dal.get_dal(ProfileDAL)
        result = profile_dal.detail(id=user.profile_id)
        return result
