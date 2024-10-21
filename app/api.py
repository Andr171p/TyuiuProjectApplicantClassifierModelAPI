from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.model_schema import (
    ModelPredictSchema,
    APIResponseModelPredictSchema,
    APIResponseModelPredictAllSchema
)
from app.schemas.user_schema import (
    UserSchema,
    UsersSchema
)
from app.utils import create_user

from ml.model import BinaryClassifierModel

from client.user import User
from client.process import UserProcessing, UsersProcessing

from typing import List


router = APIRouter()


model = BinaryClassifierModel()


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
async def predict_user(user: UserSchema) -> JSONResponse:
    user = create_user(user=user)
    user_processing = UserProcessing(user=user)
    processed_user = user_processing.process_user()
    prediction = model.predict(x=processed_user)
    prediction_response = ModelPredictSchema.model_validate(prediction)
    return JSONResponse(
        content={
            "status": "ok",
            "data": prediction_response.model_dump()
        }
    )


@router.post(path="/predict_users/", response_model=APIResponseModelPredictAllSchema)
async def predict_users(users: UsersSchema) -> JSONResponse:
    list_of_users: List[User] = []
    for user in users.users:
        user = create_user(user=user)
        list_of_users.append(user)
    users_processing = UsersProcessing(users=list_of_users)
    processed_users = users_processing.process_users()
    predictions = model.predict(x=processed_users)
    return JSONResponse(
        content={
            "status": "ok",
            "data": predictions
        }
    )
