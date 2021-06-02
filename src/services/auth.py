import time
from typing import Optional
import documents
from loaders import loader
from jose import JWTError, jwt
from configs.config import config
from fastapi import HTTPException, status, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.user import UserService


class JWTBearer(HTTPBearer):
    def __init__(self):
        super(JWTBearer, self).__init__(auto_error=True)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")


async def create_access_token(account: str, expires_delta: Optional[time.time] = None):
    if expires_delta:
        expire = time.time()
    else:
        expire = time.time() + 15
    return jwt.encode(
        {
            'account': account,
            'expire': expire
        },
        config().auth.secret_key,
        config().auth.algorithm
    )


async def get_current_user(token: str = Depends(JWTBearer())):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config().auth.secret_key, algorithms=[
            config().auth.algorithm])
        account: str = payload.get("account")
        if account is None:
            raise credentials_exception
        token_data = documents.TokenData(account=account)
    except JWTError:
        raise credentials_exception

    async with loader.db_session() as session:
        async with session.begin_nested():
            user_service = UserService(session=session)
            user = await user_service.get_user_by_account(account=token_data.account)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: documents.User = Depends(get_current_user)):
    if current_user.disable:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
