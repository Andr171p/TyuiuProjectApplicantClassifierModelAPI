import joblib

from typing import Any

from service.utils import get_root_path


class LoadModel:
    RANDOM_FORREST_MODEL_PATH = fr"{get_root_path()}/ml/models/random_forrest_model.joblib"
    LOGISTIC_REGRESSION_MODEL_PATH = fr"{get_root_path()}/ml/models/logistic_regression_model.joblib"

    @classmethod
    def load_random_forrest_model(cls) -> Any:
        model = joblib.load(filename=cls.RANDOM_FORREST_MODEL_PATH)
        return model

    @classmethod
    def load_logistic_regression_model(cls) -> Any:
        model = joblib.load(filename=cls.LOGISTIC_REGRESSION_MODEL_PATH)
        return model
