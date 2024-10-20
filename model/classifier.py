from typing import Any

from model.load_model import LoadModel


class BinaryClassifierModel(LoadModel):
    def __init__(self) -> None:
        self._model = self.load_model()

    def predict(self, data: Any) -> Any:
        predicted = self._model.predict(data)
        return predicted