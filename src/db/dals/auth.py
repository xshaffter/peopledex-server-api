from datetime import timedelta, datetime
from typing import Optional

from common.fastapi.db import CRUDDal, BaseDal as Dal
from common.fastapi.core.parameters import get_param_manager
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt

from ..hash import Hash
from ..models.user import User
from ..models.token import Token

oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/token')


class AuthDAL(Dal):

    def __init__(self, *args, **kwargs):
        super(AuthDAL, self).__init__(*args, **kwargs)
        self._parameters = get_param_manager()

    def login(self, data: OAuth2PasswordRequestForm):
        user = self._db.query(User).filter(User.username == data.username).first()
        if user and Hash.verify(user.password_hash, data.password):
            return user
        raise HTTPException(400, 'Wrong username or password')

    def get_access_token(self, request: OAuth2PasswordRequestForm, expires_delta: Optional[timedelta] = None):
        user = self.login(request)
        token = self.find_token_by_user(user)
        if not token:
            token_dal = CRUDDal(self._db, Token)
            token = token_dal.get_object(user_id=user.id)
            token_str = self.create_access_token(data={'sub': user.username}, expires_delta=expires_delta)
            if not token:
                token = token_dal.create({"user_id": user.id, "token": token_str}).token
            else:
                token = token_dal.update({"token": token_str}, user_id=user.id).token
        return token

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._parameters.variables.SECRET_KEY, algorithm=self._parameters.variables.ALGORITHM)
        return encoded_jwt

    def find_token_by_user(self, user):
        token = self._db.query(Token).filter(Token.user_id == user.id).first()
        if not token:
            return None
        try:
            decoded = jwt.decode(token.token, self._parameters.variables.SECRET_KEY, algorithms=self._parameters.variables.ALGORITHM)
        except:
            return None
        if datetime.fromtimestamp(decoded.get('exp')) <= datetime.utcnow():
            return None
        return token.token