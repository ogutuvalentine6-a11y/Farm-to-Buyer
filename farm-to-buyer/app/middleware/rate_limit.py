import time
from collections import defaultdict
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

WINDOW = 60
LIMIT = 120
_buckets: dict[str, list[float]] = defaultdict(list)


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host if request.client else "unknown"
        now = time.time()
        hits = [t for t in _buckets[ip] if now - t < WINDOW]
        _buckets[ip] = hits + [now]
        if len(hits) > LIMIT:
            return JSONResponse({"detail": "Too many requests"}, status_code=429)
        return await call_next(request)
