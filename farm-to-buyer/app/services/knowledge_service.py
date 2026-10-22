from bson import ObjectId
from app.models.knowledge import Knowledge


async def create_article(contributor_id: str, data: dict) -> dict:
    k = Knowledge(contributor_id=ObjectId(contributor_id), **data)
    await k.insert()
    return _to_out(k)


async def search_articles(q: str | None = None) -> list[dict]:
    items = await Knowledge.find_all().to_list()
    if q:
        items = [i for i in items if q.lower() in i.title.lower() or q.lower() in i.body.lower()]
    return [_to_out(i) for i in items]


def _to_out(k: Knowledge) -> dict:
    return {
        "id": str(k.id), "contributor_id": str(k.contributor_id), "title": k.title,
        "category": k.category, "body": k.body, "sources": k.sources,
        "is_verified": k.is_verified,
    }
