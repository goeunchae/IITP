
# 데이터 전처리를 위한 코드 입니다
# 이제 필요없음 
# 삭제 예정

import pickle
import pandas as pd
import os
from sklearn.model_selection import train_test_split

data_dir = './data'

data=pd.read_csv(os.path.join(data_dir, 'energydata_complete.csv'))
data.to_pickle(os.path.join(data_dir, "energydata_complete.pkl"))

x=data.drop('Appliances',axis=1)
y=data['Appliances']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=2021)

X_train.to_pickle(os.path.join(data_dir, "x_train.pkl"))
y_train.to_pickle(os.path.join(data_dir, "y_train.pkl"))

X_test.to_pickle(os.path.join(data_dir, "x_test.pkl"))
y_test.to_pickle(os.path.join(data_dir, "y_test.pkl"))

