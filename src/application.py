from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.auth.routes import auth_router
from src.database import ENGINE


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    ENGINE.dispose()


def build_app():
    app = FastAPI()

    app.include_router(auth_router)

    app.mount("/css", StaticFiles(directory="./src/static/css"), name="static")
    app.mount("/js", StaticFiles(directory="./src/static/js"), name="static")
    app.mount("/img", StaticFiles(directory="./src/static/images"), name="static")

    @app.get("/ping")
    def ping():
        return "pong"

    return app
