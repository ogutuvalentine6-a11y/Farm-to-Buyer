import pytest


@pytest.mark.anyio
async def test_list_farms(client):
    r = await client.get("/api/v1/farms/")
    assert r.status_code == 200
