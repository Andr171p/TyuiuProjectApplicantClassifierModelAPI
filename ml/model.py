from ml.load import LoadModel

from typing import Any


class BinaryClassifierModel(LoadModel):
    def __init__(self) -> None:
        self._model = self.load_random_forrest_model()

    def predict(self, x: Any) -> Any:
        predicted = self._model.predict(x)
        return predicted[0]

    def predict_probability(self, x: Any) -> Any:
        predicted = self._model.predict_proba(x)
        return predicted[0]
