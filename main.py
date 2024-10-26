from fastapi import FastAPI

from app.routers.ml import ml_router
from app.routers.docs import docs_router
from app.globals import g, GlobalMiddleware

from ml.model import BinaryClassifierModel

from contextlib import asynccontextmanager
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    model = BinaryClassifierModel()
    g.set_default("binary_classifier_model", model)
    logger.info("startup Fastapi")
    yield
    del model


def get_fastapi_app():
    fastapi_app = FastAPI(
        title="Predict applicant API",
        lifespan=lifespan
    )
    fastapi_app.include_router(
        router=ml_router,
        prefix='/ml',
        tags=['Ml']
    )
    fastapi_app.include_router(
        router=docs_router,
        tags=['Docs']
    )
    fastapi_app.add_middleware(GlobalMiddleware)
    return fastapi_app


app = get_fastapi_app()
