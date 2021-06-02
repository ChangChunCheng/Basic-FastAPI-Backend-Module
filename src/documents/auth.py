from pydantic import BaseModel


class Login(BaseModel):
    account: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    account: str
