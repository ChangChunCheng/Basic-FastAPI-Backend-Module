from datetime import timedelta
from typing import List, Optional
from fastapi import APIRouter, status, HTTPException, Depends
from configs.config import config
import documents
from loaders import loader
from services.user import UserService
from services.auth import create_access_token, get_current_active_user, get_current_user

user_router = APIRouter()


@user_router.get('/', response_model=List[documents.User], status_code=status.HTTP_200_OK)
async def get_pricipals(account: Optional[str] = None, skip: int = 0, limit: int = 10):
    async with loader.db_session() as session:
        async with session.begin_nested():
            user_service = UserService(session=session)
            if account:
                result = await user_service.get_user_by_account(account=account)
                return [result] if result else None
            else:
                return list(await user_service.get_users(skip=skip, limit=limit))


@user_router.post('/create', response_model=List[documents.User], status_code=status.HTTP_201_CREATED)
async def create_user(user: documents.UserCreate):
    try:
        async with loader.db_session() as session:
            async with session.begin_nested():
                user_service = UserService(session=session)
                await user_service.create_user(user=user)
        return await get_pricipals(account=user.account)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='User exist.')


@user_router.post("/token", response_model=documents.Token)
async def login_for_access_token(login: documents.Login = Depends()):
    async with loader.db_session() as session:
        async with session.begin_nested():
            user_service = UserService(session=session)
            user = await user_service.authenticate_user(login.account, login.password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            access_token = await create_access_token(
                account=user,  expires_delta=config().auth.access_token_expire_minutes
            )
            return documents.Token(access_token=access_token, token_type='bearer')


@user_router.get("/me")
async def read_own_items(current_user: documents.User = Depends(get_current_active_user)):
    return current_user
