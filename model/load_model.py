import joblib

from typing import Any

from misc.utils import get_root_path


class LoadModel:
    model_path = fr"{get_root_path()}\model\model.joblib"

    @classmethod
    def load_model(cls) -> Any:
        model = joblib.load(filename=cls.model_path)
        return model
