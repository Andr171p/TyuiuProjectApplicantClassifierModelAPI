from client.utils import load_columns, dict_columns

from typing import Dict, List


def user_features() -> Dict[str, List]:
    features: Dict[str, List] = dict_columns(
        columns=load_columns()
    )
    return features
