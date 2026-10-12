
from httpx import ASGITransport, AsyncClient

from myfastapi.main import app


async def _client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


async def test_partition_known_values() -> None:
    expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

    async with await _client() as client:
        for n, want in enumerate(expected):
            response = await client.get(f"/partition/{n}")

            assert response.status_code == 200
            assert response.json() == {"n": n, "p_n": want}


async def test_partition_100() -> None:
    async with await _client() as client:
        response = await client.get("/partition/100")

        assert response.status_code == 200
        assert response.json()["p_n"] == 190569292


async def test_partition_upper_boundary_and_limit() -> None:
    async with await _client() as client:
        response = await client.get("/partition/1000")

        assert response.status_code == 200
        assert response.json() == {
            "n": 1000,
            "p_n": 24061467864032622473692149727991,
        }

        response = await client.get("/partition/1001")

        assert response.status_code == 400
        assert response.json()["detail"] == "n must be <= 1000"


async def test_partition_rejects_negative() -> None:
    async with await _client() as client:
        response = await client.get("/partition/-1")

        assert response.status_code == 400
        assert response.json()["detail"] == "n must be non-negative"
