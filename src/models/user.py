import uuid

from sqlalchemy.sql.sqltypes import Boolean
from .common import DB_BASE
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(DB_BASE):
    __tablename__: str = 'users'

    id: Column = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4()
    )

    name: Column = Column(
        String(5)
    )

    account: Column = Column(
        String(50),
        primary_key=True,
        unique=True
    )

    password: Column = Column(
        String(256)
    )

    disable: Column = Column(
        Boolean,
        default=False
    )

    createat: Column = Column(
        DateTime,
        default=func.now()
    )

    updateat: Column = Column(
        DateTime,
        default=func.now()
    )
