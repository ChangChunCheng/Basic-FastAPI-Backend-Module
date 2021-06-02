from functools import lru_cache
from importlib.metadata import metadata
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from configs.config import config
import models

# Intialize config, db engine and session with async


class PqslLoader():
    def __init__(self) -> None:
        self.config = config()
        echo = True if config().app.mode in {'DEVELOPMENT', 'TEST'} else False
        self.db_engine = create_async_engine(self.config.db.dsn, echo=echo)
        self.db_session = sessionmaker(
            self.db_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def model_create(self):
        async with self.db_engine.begin() as engine:
            await engine.run_sync(models.User.metadata.create_all)
            pass
