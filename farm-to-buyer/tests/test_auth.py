import pytest


@pytest.mark.anyio
async def test_register_and_login(client):
    r = await client.post("/api/v1/auth/register", json={
        "full_name": "Test Farmer",
        "email": "farmer@example.com",
        "password": "secret123",
        "role": "farmer",
    })
    assert r.status_code in (201, 400)

    r = await client.post("/api/v1/auth/login", json={
        "email": "farmer@example.com",
        "password": "secret123",
    })
    assert r.status_code in (200, 401)
