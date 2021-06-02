from pydantic import BaseModel


class App_Config(BaseModel):
    maintainer: str = 'Jacky Chang'
    email: str = 'jacky850509@gmail.com'
    mode: str = 'DEVELOPMENT'
