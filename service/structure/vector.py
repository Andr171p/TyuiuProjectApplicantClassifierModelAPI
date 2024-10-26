from service.user.user import User
from service.user.features import user_features
from service.utils import replace_nan

from typing import Dict, List

from pandas import DataFrame

from loguru import logger


class UserVector:
    data: Dict[str, List] | None = None

    def __init__(self, user: User) -> None:
        self.user = user
        logger.info(self.user)

    def insert_user(self) -> None:
        self.data = user_features()
        self.data['Пол'].append(self.user.gender)
        self.data['Нуждается в общежитии'].append(self.user.needs_hostel)
        self.data['Ср. балл док-та об образовании'].append(self.user.average_rate)
        self.data['Приоритет'].append(self.user.priority)
        self.data['Сумма баллов'].append(self.user.total_exam_points)
        self.data['Сумма баллов за индивидуальные достижения'].append(self.user.total_bonus_points)
        self.data[f'Полученное образование_{self.user.education}'].append(True)
        self.data[f'Форма обучения_{self.user.form_of_education}'].append(True)
        self.data[f'Вид приема_{self.user.type_of_reception}'].append(True)
        self.data[f'Направление подготовки_{self.user.speciality}'].append(True)
        self.data = replace_nan(dict_data=self.data)
        logger.info(self.data)

    def get_user(self) -> DataFrame:
        user = DataFrame().from_dict(data=self.data)
        self.data = None
        return user
