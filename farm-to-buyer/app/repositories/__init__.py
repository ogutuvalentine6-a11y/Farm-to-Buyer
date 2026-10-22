from typing import Any, Type
from beanie import Document


class BaseRepository:
    def __init__(self, model: Type[Document]):
        self.model = model

    async def get(self, id: str) -> Document | None:
        return await self.model.get(id)

    async def list(self, **filters: Any) -> list[Document]:
        return await self.model.find(filters or {}).to_list()

    async def create(self, data: dict) -> Document:
        obj = self.model(**data)
        await obj.insert()
        return obj

    async def delete(self, id: str) -> bool:
        obj = await self.model.get(id)
        if not obj:
            return False
        await obj.delete()
        return True
