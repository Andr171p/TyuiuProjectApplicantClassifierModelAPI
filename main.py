import uvicorn

from fastapi import FastAPI

from app.api import router
from app.settings.network import AppNetwork


app = FastAPI(
    title="Predict applicant API"
)

app.include_router(
    router=router,
    prefix="/api/applicant_classifier_service",
    tags=["applicant_classifier_service"]
)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=AppNetwork.HOST,
        port=AppNetwork.PORT
    )
