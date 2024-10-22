from client.utils import load_columns, dict_from_str_list

from typing import Dict, List

from loguru import logger


class UserFeatures:
    features: Dict[str, List] = dict_from_str_list(
        str_list=load_columns()
    )
