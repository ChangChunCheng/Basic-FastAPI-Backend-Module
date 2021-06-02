from apis.api import app
from loaders import startup


@app.on_event('startup')
async def on_startup():
    await startup()


@app.get("/")
async def home():
    return 'Hello World!'
