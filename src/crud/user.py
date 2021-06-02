from typing import List, Optional, AsyncIterator, AsyncGenerator, MutableMapping, Mapping
from models.user import User
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, insert, update, delete
from sqlalchemy.sql import func


class UserControl(User):
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_users(self, skip: Optional[int] = 0, limit: Optional[int] = 10) -> MutableMapping[User.__tablename__, User]:
        stamt_users = select(
            User
        ).select_from(
            User
        ).offset(
            offset=skip
        ).limit(
            limit=limit
        )
        users = await self.session.execute(stamt_users)
        return users.fetchall()

    async def get_user_by_account(self, account: User.account) -> Mapping[User.__tablename__, User]:
        stamt_user = select(
            User
        ).select_from(
            User
        ).where(
            User.account == account
        )
        user = await self.session.execute(stamt_user)
        return user.fetchone()

    async def create_user(self, user: User) -> None:
        print(user)
        stamt_user = insert(User).values(user.dict())
        stamt_user.execution_options(synchronize_session='fetch')
        await self.session.execute(stamt_user)
        await self.session.flush()
        await self.session.commit()
        return None
