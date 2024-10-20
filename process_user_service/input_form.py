from misc.utils import (
    load_columns,
    dict_from_str_list
)

from typing import Dict, List


class InputForm:
    @staticmethod
    def form() -> Dict[str, List]:
        columns = load_columns()
        form = dict_from_str_list(str_list=columns)
        return form
