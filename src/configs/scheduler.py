# from pydantic import BaseModel
from pytz import utc

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


class APScheduler_Config():
    jobstores = {
        'mongo': MemoryJobStore(),
        'default': SQLAlchemyJobStore(url='sqlite:///../db/scheduler/scheduler.sqlite')
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }
    timezone = utc
