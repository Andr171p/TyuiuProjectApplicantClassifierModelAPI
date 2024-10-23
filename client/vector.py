from client.user import User
from client.features import user_features
from client.utils import replace_nan

from typing import Any, Dict, List

from pandas import DataFrame

from loguru import logger


class UserVector:
    features: Dict[str, List] | None = None

    def __init__(self, user: User) -> None:
        self.user = user
        logger.info(self.user)

    def insert(self) -> None:
        self.features = user_features()
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
        self.features = replace_nan(dict_data=self.features)
        logger.info(self.features)

    def dataframe(self) -> DataFrame:
        dataframe = DataFrame(data=self.features)
        self.features = None
        return dataframe

