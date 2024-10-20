import numpy as np
import pandas as pd
from pandas import DataFrame

from misc.utils import binary_encode


BINARY_COLUMNS = ['Пол', 'Нуждается в общежитии']

UNIQUE_BINARY_VALUES = [['М', 'Ж'], ['да', 'нет']]


class EncodeInputData:
    def __init__(self, data: DataFrame) -> None:
        self._data = data

    def binary_encoding(self) -> DataFrame | None:
        for column, values in zip(BINARY_COLUMNS, UNIQUE_BINARY_VALUES):
            self._data = binary_encode(
                data=self._data,
                column=column,
                unique_values=values
            )
        return self._data

    def categorical_encoding(self) -> DataFrame | None:
        self._data['Служба в армии'] = self._data['Служба в армии'].apply(
            lambda x: 0 if x == 'нет' else 1
        )
        self._data['Спорт'] = self._data['Спорт'].apply(
            lambda x: 0 if pd.isna(x) else 1
        )
        return self._data

