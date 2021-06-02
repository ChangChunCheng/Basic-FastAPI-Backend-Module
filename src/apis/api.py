'''
# Build the blueprint in this script
'''

from fastapi import FastAPI
from configs.config import config
from .user import user_router

# Define FastAPI APP


def create_app():
    if str(config().app.mode).upper() in {'DEVELOPMENT', 'TEST'}:
        app = FastAPI()
    else:
        app = FastAPI(docs_url='/docs', redoc_url='/redoc', openapi_url=None)
    return app


app = create_app()

app.include_router(user_router, prefix=config().router.user_router)
