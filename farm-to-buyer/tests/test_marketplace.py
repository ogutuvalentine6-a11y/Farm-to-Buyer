import pytest


@pytest.mark.anyio
async def test_list_produce(client):
    r = await client.get("/api/v1/produce/")
    assert r.status_code == 200
