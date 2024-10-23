from client.utils import load_columns, dict_columns

from typing import Dict, List


class UserFeatures:
    features: Dict[str, List] = dict_columns(
        columns=load_columns()
    )
