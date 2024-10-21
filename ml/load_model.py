import joblib

from typing import Any

from client.utils import get_root_path


class LoadModel:
    RANDOM_FORREST_MODEL_PATH = fr"{get_root_path()}/model/random_forrest_model.joblib"

    @classmethod
    def load_random_forrest_model(cls) -> Any:
        model = joblib.load(filename=cls.RANDOM_FORREST_MODEL_PATH)
        return model
