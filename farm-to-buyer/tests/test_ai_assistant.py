import pytest


@pytest.mark.anyio
async def test_ai_requires_auth(client):
    r = await client.post("/api/v1/ai/chat", json={"message": "How do I plant maize?"})
    assert r.status_code in (401, 403)
