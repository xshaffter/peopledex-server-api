from typing import Dict

from fastapi import Body
from pydantic import BaseModel, model_validator

from ..db.models.profile import Profile


class UserBasicModel(BaseModel):
    username: str

    class Config:
        from_attributes = True


class UserRegisterData(BaseModel):
    profile_id: int
    username: str
    password: str


class UserData(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    access_token: str
    user: UserData


class ChangePasswordSchema(BaseModel):
    password: str
    password_confirm: str

    @model_validator(mode='after')
    def validator(self, values) -> Dict:
        assert values["password"] == values["password_confirm"], "Las contraseñas deben coincidir"
        return values


class UserSchema(BaseModel):
    id: int
    username: str
    profile_id: int

    class Config:
        from_attributes = True


class UserRequestSchema(BaseModel):
    username: str
    profile_id: int
    password_hash: str

    class Config:
        model = Profile
