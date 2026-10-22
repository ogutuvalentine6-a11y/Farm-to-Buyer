import pytest


@pytest.mark.anyio
async def test_mpesa_callback_accepts(client):
    r = await client.post("/api/v1/payments/mpesa/callback", json={"Body": {}})
    assert r.status_code == 200
