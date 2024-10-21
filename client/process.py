from client.vector import UserVector
from client.matrix import UserMatrix

from client.preprocessing import binary, standard

from pandas import DataFrame


class UserProcessing(UserVector):

    def add_user(self) -> DataFrame:
        self.insert()
        user_dataframe = self.dataframe()
        return user_dataframe

    def process_user(self) -> DataFrame:
        user_dataframe = self.add_user()
        user_dataframe = binary(dataframe=user_dataframe)
        user_dataframe = standard(dataframe=user_dataframe)
        return user_dataframe


class UsersProcessing(UserMatrix):
    def add_users(self) -> DataFrame:
        self.insert()
        users_dataframe = self.dataframe()
        return users_dataframe

    def process_users(self) -> DataFrame:
        users_dataframe = self.add_users()
        users_dataframe = binary(dataframe=users_dataframe)
        users_dataframe = standard(dataframe=users_dataframe)
        return users_dataframe
