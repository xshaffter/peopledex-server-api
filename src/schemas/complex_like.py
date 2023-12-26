from datetime import date
from typing import Optional

from pydantic import BaseModel

from ..db.models.complex_like import ComplexLike


class ComplexLikeSchema(BaseModel):
    name: str
    favorite: str

    class Config:
        from_attributes = True


class ComplexLikeRequestSchema(BaseModel):
    name: str
    favorite: str
    profile_id: int

    class Config:
        model = ComplexLike
