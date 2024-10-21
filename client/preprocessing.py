import numpy as np

from pandas import DataFrame

from sklearn.preprocessing import normalize


def binary(dataframe: DataFrame) -> DataFrame:
    BINARY_COLUMNS = ['Пол', 'Нуждается в общежитии']
    UNIQUE_BINARY_VALUES = [['М', 'Ж'], ['да', 'нет']]
    for column, values in zip(BINARY_COLUMNS, UNIQUE_BINARY_VALUES):
        value_0, value_1 = values
        dataframe[column] = dataframe[column].replace(
            {
                value_0: 0,
                value_1: 1
            }
        )
    return dataframe


def standard(dataframe: DataFrame) -> DataFrame:
    dataframe = normalize(dataframe)
    return dataframe
