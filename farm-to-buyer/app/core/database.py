from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings

_client: AsyncIOMotorClient | None = None


async def init_db(document_models):
    global _client
    _client = AsyncIOMotorClient(settings.MONGODB_URI)
    await init_beanie(database=_client[settings.MONGODB_DB], document_models=document_models)


async def close_db():
    global _client
    if _client:
        _client.close()
        _client = None
