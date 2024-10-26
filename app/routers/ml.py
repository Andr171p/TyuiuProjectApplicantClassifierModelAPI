from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.globals import g
from app.schemas.user import (
    UserSchema,
    UsersSchema
)
from app.schemas.api import (
    APIResponseModelPredictionSchema,
    APIResponseModelPredictionsSchema
)

from service.user.user import (
    User,
    Users
)
from service.process import (
    UserProcessing,
    UsersProcessing
)


ml_router = APIRouter()


@ml_router.post(path='/predict_user/', response_model=APIResponseModelPredictionSchema)
async def predict_user(user: UserSchema) -> JSONResponse:
    user = User.model_validate(user.model_dump())
    model = g.binary_classifier_model
    processed_user = UserProcessing(user=user).process_user()
    prediction = model.predict_probability(x=processed_user)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': prediction
        }
    )


@ml_router.post(path='/predict_users/', response_model=APIResponseModelPredictionsSchema)
async def predict_users(users: UsersSchema) -> JSONResponse:
    users = Users.model_validate(users.model_dump())
    model = g.binary_classifier_model
    precessed_users = UsersProcessing(users=users).process_users()
    predictions = model.predict_probability(x=precessed_users)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': predictions
        }
    )
