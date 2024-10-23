from client.features import user_features
from client.user import User
from client.utils import replace_nan

from typing import Dict, List

from pandas import DataFrame


class UserMatrix:
    features: Dict[str, List] | None = None

    def __init__(self, users: List[User]) -> None:
        self.users = users

    def insert(self) -> None:
        self.features = user_features()
        for user in self.users:
            self.features['Пол'].append(user.gender)
            self.features['Нуждается в общежитии'].append(user.needs_hostel)
            self.features['Ср. балл док-та об образовании'].append(user.average_rate)
            self.features['Приоритет'].append(user.priority)
            self.features['Сумма баллов'].append(user.total_exam_points)
            self.features['Сумма баллов за индивидуальные достижения'].append(user.total_bonus_points)
            self.features[f'Полученное образование_{user.education}'].append(True)
            self.features[f'Форма обучения_{user.form_of_education}'].append(True)
            self.features[f'Вид приема_{user.type_of_reception}'].append(True)
            self.features[f'Направление подготовки_{user.speciality}'].append(True)
            self.features = replace_nan(dict_data=self.features)
            print(self.features)

    def dataframe(self) -> DataFrame:
        dataframe = DataFrame(data=self.features)
        self.features = None
        return dataframe
