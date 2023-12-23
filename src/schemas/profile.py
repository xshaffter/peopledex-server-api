from datetime import date
from typing import Optional

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

    class Config:
        model = Profile
