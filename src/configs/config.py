from functools import lru_cache
from pydantic import BaseSettings
from .app import App_Config
from .psql import DB_Config
from .auth import Auth_Config
from .router import Router_Config


class Config(BaseSettings):
    app: App_Config = App_Config()
    db: DB_Config = DB_Config()
    auth: Auth_Config = Auth_Config()
    router: Router_Config = Router_Config()


@lru_cache
def config():
    return Config()
