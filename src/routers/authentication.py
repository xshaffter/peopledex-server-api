from common.fastapi.db import get_dal_dependency
from common.fastapi.routing import BaseRouter, post
from common.fastapi.schemas import HTTPResponseModel, HTTP_200_UPDATED
from fastapi import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from src.db.dals.auth import AuthDAL, oauth2_schema
from src.db.dals.user import UserDAL
from src.schemas.user import TokenData, ChangePasswordSchema


class AuthRouter(BaseRouter):

    @post('/token', response_model=TokenData)
    def get_token(self, request: OAuth2PasswordRequestForm = Depends(),
                  dal: AuthDAL = Depends(get_dal_dependency(AuthDAL))):
        token = dal.get_access_token(request)
        user = dal.login(request)
        return {
            'user': user,
            'access_token': token,
        }

    @post('/password_change', response_model=HTTPResponseModel)
    def change_password(self, request: ChangePasswordSchema, dal: UserDAL = Depends(get_dal_dependency(UserDAL)),
                        token: str = Depends(oauth2_schema)):
        dal.change_password(dict(password=request.password), token)
        return HTTP_200_UPDATED
