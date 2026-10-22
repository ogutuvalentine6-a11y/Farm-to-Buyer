import pytest


@pytest.mark.anyio
async def test_list_my_orders_unauthenticated(client):
    r = await client.get("/api/v1/orders/mine")
    assert r.status_code in (401, 403)
