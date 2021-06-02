# from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base


class Common:

    def __init__(self):
        pass

    # sqlalchemy model to dict in order to build pydantic model
    def dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items() if key in self.__table__.columns}


DB_BASE = declarative_base()
DB_BASE.dict = Common.dict
