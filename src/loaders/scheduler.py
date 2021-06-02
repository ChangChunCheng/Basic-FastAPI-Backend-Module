from functools import lru_cache
from configs.config import config

from jobs.show import show

from apscheduler.schedulers.asyncio import AsyncIOScheduler


@lru_cache
def scheduler():
    scheduler = AsyncIOScheduler(
        jobstores=config().scheduler.jobstores,
        executors=config().scheduler.executors,
        job_defaults=config().scheduler.job_defaults,
        timezone=config().scheduler.timezone
    )
    scheduler.add_job(show, 'interval', seconds=3)
    return scheduler
