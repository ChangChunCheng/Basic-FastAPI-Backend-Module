from .psql import PqslLoader


loader = PqslLoader()

# Setting the startup jobs


async def startup():
    await loader.model_create()
