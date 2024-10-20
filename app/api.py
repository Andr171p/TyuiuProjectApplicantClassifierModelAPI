from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.model_schema import (
    APIResponseModelPredictSchema
)
from app.schemas.user_schema import UserSchema

from app.user import User

from process_user_service.input_data import InputData

router = APIRouter()


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
    _user = User()