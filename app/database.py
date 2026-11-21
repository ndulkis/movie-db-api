from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    mongo_uri: str
    db_name: str


settings = Settings()
client = AsyncIOMotorClient(settings.mongo_uri)
movies = client[settings.db_name]["movies"]


async def create_indexes():
    await movies.create_index([("title", "text")])  # search by title
    await movies.create_index("genre")              # filter by genre
    await movies.create_index("release_date")       # filter/sort by year
