'''
# Build the blueprint in this script
'''
import time
from fastapi import FastAPI, Request
from configs.config import config
from .user import user_router


def create_app():
    if str(config().app.mode).upper() in {'DEVELOPMENT', 'TEST'}:
        app = FastAPI()
    else:
        app = FastAPI(docs_url='/docs', redoc_url='/redoc', openapi_url=None)
    return app


root = None


def init_middleware(app):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


def init():
    app = create_app()
    init_middleware(app)
    return app


app = init()
app.include_router(user_router, prefix=config().router.user_router)
