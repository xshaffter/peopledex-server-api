from typing import List

from common.fastapi.db import CRUDDal, get_dal_dependency
from common.fastapi.routing import GenericBaseCRUDRouter, get
from fastapi import Depends

from ..db.models.complex_like import ComplexLike
from ..db.models.profile import Profile
from ..schemas.complex_like import ComplexLikeSchema, ComplexLikeRequestSchema
from ..schemas.profile import ProfileRequestSchema, ProfileSchema, SimplifiedProfileSchema


class ComplexLikeRouter(GenericBaseCRUDRouter[ComplexLike, ComplexLikeSchema, ComplexLikeRequestSchema]):
    ...
