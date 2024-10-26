from pydantic import BaseModel

from typing import List, Literal

from app.schemas.model import ModelPredictionSchema


class APIResponseModelPredictionSchema(BaseModel):
    status: Literal['ok'] = 'ok'
    data: ModelPredictionSchema


class APIResponseModelPredictionsSchema(BaseModel):
    status: Literal['ok'] = 'ok'
    data: List[ModelPredictionSchema]
