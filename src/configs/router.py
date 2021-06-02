from pydantic import BaseModel


class Router_Config(BaseModel):
    user_router: str = '/user'

    token_url: str = user_router + '/token'
