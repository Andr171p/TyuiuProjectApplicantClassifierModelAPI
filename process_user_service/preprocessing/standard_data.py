import numpy as np

from pandas import DataFrame

from sklearn.preprocessing import normalize


class StandardInputData:
    def __init__(self, data: DataFrame) -> None:
        self._data = data

    def normalize(self) -> np.array:
        data = normalize(self._data)
        return data