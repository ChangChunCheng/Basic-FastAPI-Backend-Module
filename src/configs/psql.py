from pydantic import BaseModel


class DB_Config(BaseModel):
    # PostgreSQL host IP
    host: str = '127.0.0.1'
    # PostgreSQL port
    port: int = 5432
    user: str = 'postgresql'
    password: str = 'postgresql'
    db: str = 'test'
    dsn: str = 'postgresql+asyncpg://' \
        + user \
        + ':' \
        + password \
        + '@' \
        + host \
        + ':' \
        + str(port) \
        + '/' \
        + db
