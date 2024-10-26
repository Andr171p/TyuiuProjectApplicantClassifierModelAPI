from pandas import DataFrame

from sklearn.preprocessing import normalize


def binary(dataframe: DataFrame) -> DataFrame:
    print(dataframe)
    dataframe['Пол'] = dataframe['Пол'].apply(
        lambda x: 1 if x == 'М' else 0
    )
    dataframe['Нуждается в общежитии'] = dataframe['Нуждается в общежитии'].apply(
        lambda x: 1 if x == 'да' else 0
    )
    return dataframe


def standard(dataframe: DataFrame) -> DataFrame:
    dataframe = normalize(dataframe)
    return dataframe
