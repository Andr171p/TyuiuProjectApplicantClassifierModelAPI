from pandas import DataFrame

from misc.utils import (
    load_columns,
    dict_from_str_list,
    df_from_dict,
    add_false_to_dict
)

from typing import Dict, List

from app.user import User


class InputForm:
    @staticmethod
    def form() -> Dict[str, List]:
        columns = load_columns()
        form = dict_from_str_list(str_list=columns)
        return form


class InputData:
    _input_form: Dict[str, List] = InputForm.form()

    def __init__(self, user: User) -> None:
        self._user = user

    def _add(self) -> None:
        self._input_form['Пол'].append(self._user.gender)
        self._input_form['Нуждается в общежитии'].append(self._user.needs_hostel)
        self._input_form['Ср. балл док-та об образовании'].append(self._user.average_rate)
        self._input_form['Приоритет'].append(self._user.priority)
        self._input_form['Сумма баллов'].append(self._user.total_exam_points)
        self._input_form['Сумма баллов за индивидуальные достижения'].append(self._user.total_bonus_points)
        self._input_form[f'Полученное образование_{self._user.education}'].append(True)
        self._input_form[f'Форма обучения_{self._user.form_of_education}'].append(True)
        self._input_form[f'Вид приема_{self._user.type_of_reception}'].append(True)
        self._input_form[f'Направление подготовки_{self._user.speciality}'].append(True)

    def data(self) -> DataFrame:
        self._add()
        self._input_form = add_false_to_dict(dict_data=self._input_form)
        dataframe = df_from_dict(dict_data=self._input_form)
        return dataframe

