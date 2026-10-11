from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from myfastapi.partition import partition

router = APIRouter()


class PartitionResponse(BaseModel):
    n: int
    p_n: int


@router.get("/{n}", response_model=PartitionResponse)
async def get_partition(n: int) -> PartitionResponse:
    """Return p(n), the number of integer partitions of n.

    Exact for 0 <= n <= 1000.
    """
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    if n > 1000:
        raise HTTPException(status_code=400, detail="n must be <= 1000")
    return PartitionResponse(n=n, p_n=partition(n))
