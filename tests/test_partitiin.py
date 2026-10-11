from httpx import ASGITransport, AsyncClient
from myfastapi.main import app


async def _client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


async def test_partition_known_values() -> None:
    expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
    async with await _client() as c:
        for n, want in enumerate(expected):
            r = await c.get(f"/partition/{n}")
            assert r.status_code == 200
            assert r.json() == {"n": n, "p_n": want}


async def test_partition_100() -> None:
    async with await _client() as c:
        r = await c.get("/partition/100")
        assert r.status_code == 200
        assert r.json()["p_n"] == 190569292


async def test_partition_rejects_negative() -> None:
    async with await _client() as c:
        r = await c.get("/partition/-1")
        assert r.status_code == 400
