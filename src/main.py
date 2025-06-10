import os
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase
from auth.routes import auth_router


class AlchemyBaseModel(DeclarativeBase):
    metadata = MetaData(schema="main")


load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    connection_url = URL.create(
        os.getenv("DATABASE_DIALECT"),
        username=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        database=os.getenv("DATABASE_NAME"),
    )

    engine = create_engine(connection_url, echo=True)
    yield
    engine.dispose()


def build_app():
    app = FastAPI()

    app.include_router(auth_router)

    @app.get("/ping")
    def ping():
        return "pong"

    return app


if __name__ == "__main__":
    uvicorn.run(
        "main:build_app",
        port=int(os.getenv("SERVER_PORT", 1818)),
        host=os.getenv("SERVER_HOST"),
        proxy_headers=True,
        forwarded_allow_ips="*",
        factory=True,
    )
