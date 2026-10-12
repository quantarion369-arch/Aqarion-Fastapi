from httpx import ASGITransport, AsyncClient

from myfastapi.main import app


async def _client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


async def test_asymptotic_returns_all_fields() -> None:
    async with await _client() as c:
        r = await c.get("/asymptotic/100")
        assert r.status_code == 200
        body = r.json()
        assert body["n"] == 100
        assert body["exact"] == 190569292
        assert body["approximation"] > 0
        assert 0 < body["relative_error"] < 1


async def test_asymptotic_improves_with_n() -> None:
    """Relative error of the leading term should shrink as n grows."""
    async with await _client() as c:
        r10 = (await c.get("/asymptotic/10")).json()
        r100 = (await c.get("/asymptotic/100")).json()
        assert r100["relative_error"] < r10["relative_error"]
