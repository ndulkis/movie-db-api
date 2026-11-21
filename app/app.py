from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_indexes
from app.routers import movies


@asynccontextmanager
async def lifespan(app):
    await create_indexes()
    yield


app = FastAPI(lifespan=lifespan)

# bring in all routes from movies router file
app.include_router(movies.router)


@app.get("/")
def health_check():
    return {"status": "ok"}
