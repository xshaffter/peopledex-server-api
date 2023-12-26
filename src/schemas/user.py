from pydantic import BaseModel

from ..db.models.profile import Profile


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
