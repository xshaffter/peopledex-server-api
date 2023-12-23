from common.fastapi.core.app import main_app, execute
from fastapi import status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .routers.profile import ProfileRouter
from .routers.statics import StaticsRouter

main_app.include_router(ProfileRouter(prefix='/profiles', tags=['profiles']))

main_app.include_router(StaticsRouter(prefix='/statics', tags=['statics']))


# noinspection PyUnusedLocal
@main_app.exception_handler(HTTPException)
def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)


# noinspection PyUnusedLocal
@main_app.exception_handler(RequestValidationError)
def http_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.errors())


# noinspection PyUnusedLocal
@main_app.exception_handler(ValidationError)
def http_exception_handler(request, exc: ValidationError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=exc.errors())


@main_app.get("/")
async def main():
    return 'is running'


def start():
    execute()