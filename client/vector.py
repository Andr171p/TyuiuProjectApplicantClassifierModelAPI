from client.user import User
from client.features import UserFeatures
from client.utils import add_false_to_dict

from typing import Any

from pandas import DataFrame


class UserVector(UserFeatures):
    def __init__(self, user: User) -> None:
        self.user = user

    def insert(self) -> None:
        self.features['Пол'].append(self.user.gender)
        self.features['Нуждается в общежитии'].append(self.user.needs_hostel)
        self.features['Ср. балл док-та об образовании'].append(self.user.average_rate)
        self.features['Приоритет'].append(self.user.priority)
        self.features['Сумма баллов'].append(self.user.total_exam_points)
        self.features['Сумма баллов за индивидуальные достижения'].append(self.user.total_bonus_points)
        self.features[f'Полученное образование_{self.user.education}'].append(True)
        self.features[f'Форма обучения_{self.user.form_of_education}'].append(True)
        self.features[f'Вид приема_{self.user.type_of_reception}'].append(True)
        self.features[f'Направление подготовки_{self.user.speciality}'].append(True)
        self.features = add_false_to_dict(dict_data=self.features)
        print(self.features)

    def dataframe(self) -> DataFrame:
        dataframe = DataFrame(data=self.features)
        return dataframe

