from .psql import PqslLoader
from .scheduler import scheduler

loader = PqslLoader()
scheduler = scheduler()

# Setting the startup jobs


async def startup():
    await loader.model_create()
    scheduler.start()
