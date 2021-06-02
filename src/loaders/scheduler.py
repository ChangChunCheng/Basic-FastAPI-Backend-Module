from functools import lru_cache
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from jobs.show import show


@lru_cache
def scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(show, 'interval', seconds=60)
    return scheduler
