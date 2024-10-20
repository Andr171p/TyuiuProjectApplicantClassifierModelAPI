from pandas import DataFrame

from process_user_service.input_form import InputForm

from misc.utils import (
    df_from_dict,
    add_false_to_dict
)

from typing import Dict, List

from app.user import User


class InputData:
    _input_form: Dict[str, List] = InputForm.form()

    def __init__(self, user: User) -> None:
        self._user = user

    def add_data(self) -> None:
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

    def input_data(self) -> DataFrame:
        self._input_form = add_false_to_dict(dict_data=self._input_form)
        dataframe = df_from_dict(dict_data=self._input_form)
        return dataframe


us = User(
    gender='М',
    needs_hostel='нет',
    average_rate=4.9,
    priority=1,
    total_exam_points=300,
    total_bonus_points=10,
    education='Высшее образование - магистратура',
    form_of_education='Заочная',
    type_of_reception='Общий конкурс',
    speciality='15.03.01 Машиностроение'
)
inp = InputData(user=us)
inp.add_data()
data = inp.input_data()
from process_user_service.preprocessing.encode_data import EncodeInputData
encode_data = EncodeInputData(data=data)
df = encode_data.binary_encoding()
# df = encode_data.categorical_encoding()
from process_user_service.preprocessing.standard_data import StandardInputData
data = StandardInputData(data=df).normalize()
from model.classifier import BinaryClassifierModel
print(BinaryClassifierModel().predict(data=data))