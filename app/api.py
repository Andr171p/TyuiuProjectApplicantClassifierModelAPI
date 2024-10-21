from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.model_schema import (
    APIResponseModelPredictSchema,
    APIResponseModelPredictAllSchema
)
from app.manager import (
    add_user,
    preprocessing_user
)
from app.schemas.user_schema import UserSchema
from app.validates.user_validate import UserValidate

from ml.model import BinaryClassifierModel

from typing import List


router = APIRouter()


model = None


@router.on_event("startup")
def startup_event() -> None:
    global model
    model = BinaryClassifierModel()


@router.get(path="/")
async def get_hello_world() -> JSONResponse:
    return JSONResponse(
        content={
            "status": "ok",
            "data": "Hello, world!"
        }
    )


@router.post(path="/predict_user/", response_model=APIResponseModelPredictSchema)
async def post_predict_user(user: UserSchema) -> JSONResponse:
    _user = await add_user(user=user)
    preprocessed_user = await preprocessing_user(user=_user)
    predicted_user = model.predict(preprocessed_user)
    return JSONResponse(
        content={
            "status": "ok",
            "data": predicted_user
        }
    )
