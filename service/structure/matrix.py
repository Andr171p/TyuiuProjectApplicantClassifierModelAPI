from service.user.user import Users
from service.user.features import user_features
from service.utils import replace_nan

from typing import Dict, List

from pandas import DataFrame


class UserMatrix:
    data: Dict[str, List] | None = None

    def __init__(self, users: Users) -> None:
        self.users = users

    def insert_users(self) -> None:
        self.data = user_features()
        for user in self.users.users:
            self.data['Пол'].append(user.gender)
            self.data['Нуждается в общежитии'].append(user.needs_hostel)
            self.data['Ср. балл док-та об образовании'].append(user.average_rate)
            self.data['Приоритет'].append(user.priority)
            self.data['Сумма баллов'].append(user.total_exam_points)
            self.data['Сумма баллов за индивидуальные достижения'].append(user.total_bonus_points)
            self.data[f'Полученное образование_{user.education}'].append(True)
            self.data[f'Форма обучения_{user.form_of_education}'].append(True)
            self.data[f'Вид приема_{user.type_of_reception}'].append(True)
            self.data[f'Направление подготовки_{user.speciality}'].append(True)
            self.data = replace_nan(dict_data=self.data)
            print(self.data)

    def get_users(self) -> DataFrame:
        users = DataFrame().from_dict(data=self.data)
        self.data = None
        return users
