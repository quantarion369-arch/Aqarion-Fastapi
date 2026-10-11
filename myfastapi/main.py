from fastapi import FastAPI

from myfastapi.routers import asymptotic, items, partition

app = FastAPI(title="MyFastAPI", version="0.1.0")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, world."}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(partition.router, prefix="/partition", tags=["partition"])
app.include_router(asymptotic.router, prefix="/asymptotic", tags=["asymptotic"])
