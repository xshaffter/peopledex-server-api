from datetime import date
from typing import Optional, List

from .complex_like import ComplexLikeSchema
from ..db.models.complex_like import ComplexLike
from ..db.models.profile import Profile

from pydantic import BaseModel


class ProfileSchema(BaseModel):
    id: int
    name: Optional[str]
    height_cm: Optional[int]
    weight_kg: Optional[float]
    birth_date: Optional[date]
    image_url: str
    vertical_image_url: Optional[str]
    feet: Optional[int]
    bottoms: Optional[int]
    tops: Optional[int]
    flower: Optional[str]
    color: Optional[str]
    serie: Optional[str]
    music_group: Optional[str]
    movie: Optional[str]
    complexities: List[ComplexLikeSchema]

    class Config:
        from_attributes = True


class ProfileRequestSchema(BaseModel):
    name: Optional[str]
    height_cm: Optional[int]
    weight_kg: Optional[float]
    birth_date: Optional[date]
    image_url: str
    vertical_image_url: Optional[str]
    feet: Optional[int]
    bottoms: Optional[int]
    tops: Optional[int]
    flower: Optional[str]
    color: Optional[str]
    serie: Optional[str]
    music_group: Optional[str]
    movie: Optional[str]

    class Config:
        model = Profile


class SimplifiedProfileSchema(BaseModel):
    id: int
    name: Optional[str]
    birth_date: Optional[date]
    image_url: str
    class Config:
        from_attributes = True