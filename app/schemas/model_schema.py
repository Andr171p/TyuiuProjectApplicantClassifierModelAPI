from pydantic import (
    BaseModel,
    ConfigDict
)

from typing import Literal


class ModelPredictSchema(BaseModel):
    predict: int

    model_config = ConfigDict(from_attributes=True)


class APIResponseModelPredictSchema(BaseModel):
    status: Literal['ok'] = 'ok'
    data: ModelPredictSchema