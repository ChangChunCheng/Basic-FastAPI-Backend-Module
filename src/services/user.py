from typing import Dict, List, Optional, ChainMap
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
import models
import documents
from crud.user import UserControl
from passlib.context import CryptContext
from configs.config import config


class UserService(UserControl):

    pwd_context = CryptContext(
        schemes=config().auth.password_hash_schemes,
        deprecated="auto"
    )

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        pass

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hash_password: str):
        return self.pwd_context.verify(plain_password, hash_password)

    async def get_users(self, skip: int = 0, limit: int = 10) -> ChainMap(documents.User):
        users: List[models.User] = await super().get_users(skip=skip, limit=limit)
        users = map(
            lambda user: user['User'].dict(),
            users
        )
        return map(
            lambda user: documents.User(**user),
            users
        )

    async def get_user_by_account(self, account: str) -> documents.User:
        user: models.User = await super().get_user_by_account(account=account)
        return documents.User(**user['User'].dict()) if user else None

    async def create_user(self, user: documents.UserCreate) -> documents.User:
        new_user = user.dict()
        new_user['password'] = self.get_password_hash(
            new_user['password']
        )
        del(new_user['id'])
        await super().create_user(models.User(**new_user))
        return True

    async def authenticate_user(self, account: str, password: str) -> bool:
        user: models.User = await super().get_user_by_account(account=account)
        if not user:
            return False
        return \
            account \
            if \
            (self.verify_password(password, user['User'].password)) \
            and \
            (user['User'].disable == False) \
            else \
            False
