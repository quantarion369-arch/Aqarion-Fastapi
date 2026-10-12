import subprocess
import sys
from pathlib import Path

from httpx import ASGITransport, AsyncClient

from myfastapi.main import app


def test_partition_1000_in_fresh_process() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "from myfastapi.partition import partition; "
                "assert partition(1000) == "
                "24061467864032622473692149727991; "
                "print('BOUNDARY_PASS')"
            ),
        ],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.strip() == "BOUNDARY_PASS"


async def test_partition_endpoint_upper_boundary() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get("/partition/1000")

    assert response.status_code == 200
    assert response.json() == {
        "n": 1000,
        "p_n": 24061467864032622473692149727991,
    }


async def test_partition_endpoint_rejects_above_limit() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get("/partition/1001")

    assert response.status_code == 400
    assert response.json()["detail"] == "n must be <= 1000"
