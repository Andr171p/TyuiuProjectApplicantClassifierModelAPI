from pydantic import BaseModel, ConfigDict


class ModelPredictionSchema(BaseModel):
    predict: float

    model_config = ConfigDict(from_attributes=True)
