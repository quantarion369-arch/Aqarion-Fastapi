from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from myfastapi.asymptotic import hardy_ramanujan, relative_error
from myfastapi.partition import partition

router = APIRouter()


class AsymptoticResponse(BaseModel):
    n: int
    exact: int
    approximation: float
    relative_error: float


@router.get("/{n}", response_model=AsymptoticResponse)
async def get_asymptotic(n: int) -> AsymptoticResponse:
    """Compare p(n) with its Hardy-Ramanujan leading approximation.

    Demonstrates the PB-CORE-006 saddle regime.
    """
    if n < 1:
        raise HTTPException(status_code=400, detail="n must be >= 1")
    if n > 1000:
        raise HTTPException(status_code=400, detail="n must be <= 1000")
    exact = partition(n)
    approx = hardy_ramanujan(n)
    return AsymptoticResponse(
        n=n,
        exact=exact,
        approximation=approx,
        relative_error=relative_error(n, exact),
    )
