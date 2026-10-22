from fastapi import APIRouter, Depends
from app.core.dependencies import require_role
from app.models.user import User, Role
from app.schemas.knowledge import KnowledgeCreate, KnowledgeOut
from app.services import knowledge_service

router = APIRouter()


@router.post("/", response_model=KnowledgeOut, status_code=201)
async def add_article(payload: KnowledgeCreate, current: User = Depends(require_role(Role.CONTRIBUTOR, Role.FARMER))):
    return await knowledge_service.create_article(str(current.id), payload.model_dump())


@router.get("/", response_model=list[KnowledgeOut])
async def list_articles(q: str | None = None):
    return await knowledge_service.search_articles(q)
