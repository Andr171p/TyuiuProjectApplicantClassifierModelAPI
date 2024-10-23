import csv
from typing import Dict, List, Any
from pathlib import Path

from pandas import DataFrame


def load_columns() -> List[str]:
    root_path = Path(__file__).resolve().parents[1]
    file_path = fr"{root_path}/client/columns.csv"
    columns: List[Any] = []
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            columns.append(row[0])
        return columns


def dict_columns(columns: List[str]) -> dict:
    _dict = dict()
    for column in columns:
        _dict[column] = []
    return _dict


def df_from_dict(dict_data: Dict[str, List]) -> DataFrame:
    df = DataFrame(data=dict_data)
    return df


def replace_nan(dict_data: Dict[str, List], value: bool = False) -> dict:
    keys = dict_data.keys()
    for key in keys:
        if len(dict_data[key]) == 0:
            dict_data[key].append(value)
    return dict_data


def binary_encode(data: DataFrame, column: str, unique_values: List[str]) -> DataFrame:
    if len(unique_values) == 2:
        value_0, value_1 = unique_values
        data[column] = data[column].replace(
            {
                value_0: 0,
                value_1: 1
            }
        )
    return data


def get_root_path() -> Path:
    root_path = Path(__file__).resolve().parents[1]
    return root_path

