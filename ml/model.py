from ml.load_model import LoadModel

from typing import Any


class BinaryClassifierModel(LoadModel):
    def __init__(self) -> None:
        self._model = self.load_random_forrest_model()

    def predict(self, x: Any) -> Any:
        predicted = self._model.predict(x=x)
        return predicted[0]
