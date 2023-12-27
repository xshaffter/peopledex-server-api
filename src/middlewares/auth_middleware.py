from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response, JSONResponse


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        from common.fastapi.db import get_dal
        from src.db.dals.user import UserDAL
        passes = True
        bearer = request.headers.get("authorization", False)
        if bearer and not request.url.path.startswith("/auth"):
            passes = False
            token = bearer.replace("Bearer ", "")
            dal: UserDAL = get_dal(UserDAL)
            user = dal.get_current_user(token)
            if user:
                passes = True

        if passes:
            return await call_next(request)
        else:
            return JSONResponse(status_code=404, content=dict(detail='HTTP 404 not found'))

    def __init__(self, app, **options):
        super().__init__(app)
