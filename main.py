import pandas as pd
import numpy as np


DROP_COLUMNS = [
            'Unnamed: 0', 'Иностранный язык', 'Иностранное гражданство', 'Согласие на зачисление', 'Приказ о зачислении'
        ]

df = pd.read_csv(r"C:\Users\andre\PycharmProjects\OrderStatusService\ТИУ Абитуриенты 2019-2024 Model.csv")
df = df.drop(DROP_COLUMNS, axis=1)
print(df.columns)
df = pd.get_dummies(df)
print(df.columns)
print(df.shape)
columns = df.columns
c = columns.to_numpy()
np.savetxt("process_user_service/data/columns.csv", c, fmt='%s', encoding='utf-8')
