from pydantic import BaseModel


class KnowledgeCreate(BaseModel):
    title: str
    category: str
    body: str
    sources: list[str] = []


class KnowledgeOut(KnowledgeCreate):
    id: str
    contributor_id: str
    is_verified: bool
