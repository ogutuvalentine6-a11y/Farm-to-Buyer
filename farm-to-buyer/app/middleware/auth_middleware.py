from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.core.security import decode_token

PUBLIC_PATHS = {"/health", "/docs", "/openapi.json", "/api/v1/auth/login", "/api/v1/auth/register"}


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if path in PUBLIC_PATHS or path.startswith("/static") or path.startswith("/api/v1/payments/mpesa/callback"):
            return await call_next(request)
        auth = request.headers.get("authorization", "")
        if auth.startswith("Bearer "):
            payload = decode_token(auth[7:])
            if not payload.get("sub"):
                return JSONResponse({"detail": "Invalid token"}, status_code=401)
            request.state.user_id = payload["sub"]
            request.state.role = payload.get("role")
        return await call_next(request)
