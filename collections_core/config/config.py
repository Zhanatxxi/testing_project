from pydantic import BaseSettings, PostgresDsn


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = list(PostgresDsn.allowed_schemes) + ["postgresql+asyncpg"]


class Settings(BaseSettings):


    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "zhanat"
    POSTGRES_PASSWORD: str = "1"
    POSTGRES_DB: str = "collections_core"
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 15
    SQLALCHEMY_DATABASE_URI: AsyncPostgresDsn | None = None


    PHONE_NUMBER_REGION = "RU"


settings = Settings()
