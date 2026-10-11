from httpx import ASGITransport, AsyncClient
from myfastapi.main import app


async def _client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


async def test_root() -> None:
    async with await _client() as c:
        r = await c.get("/")
        assert r.status_code == 200
        assert r.json() == {"message": "Hello, world."}


async def test_health() -> None:
    async with await _client() as c:
        r = await c.get("/health")
        assert r.json() == {"status": "ok"}


async def test_create_and_get_item() -> None:
    async with await _client() as c:
        r = await c.post("/items/", json={"id": 1, "name": "apple"})
        assert r.status_code == 201
        r = await c.get("/items/1")
        assert r.status_code == 200
        assert r.json() == {"id": 1, "name": "apple"}
