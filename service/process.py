from service.structure.vector import UserVector
from service.structure.matrix import UserMatrix
from service.preprocessing import binary, standard

from pandas import DataFrame

from loguru import logger


class UserProcessing(UserVector):
    def add_user(self) -> DataFrame:
        self.insert_user()
        user = self.get_user()
        return user

    def process_user(self) -> DataFrame:
        user = self.add_user()
        user = binary(dataframe=user)
        user = standard(dataframe=user)
        return user


class UsersProcessing(UserMatrix):
    def add_users(self) -> DataFrame:
        self.insert_users()
        users = self.get_users()
        return users

    def process_users(self) -> DataFrame:
        users = self.add_users()
        users = binary(dataframe=users)
        users = standard(dataframe=users)
        logger.info(users)
        return users


from service.user.user import User

user = User(
    gender="М",
    needs_hostel="да",
    average_rate=5.0,
    priority=1,
    total_exam_points=210,
    total_bonus_points=10,
    education="Среднее общее образование",
    form_of_education="Очная",
    type_of_reception="Общий конкурс",
    speciality="20.03.01 Техносферная безопасность"
)

print(UserProcessing(user=user).process_user())