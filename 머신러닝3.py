import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1
from sklearn.preprocessing import MinMaxScaler
# 2
# from sklearn.preprocessing import StandardScaler
# 3
# from sklearn.preprocessing import Binarizer
# 4
from sklearn.linear_model import  LinearRegression
col_names = ['preg','plas', 'pres','skin','test', 'mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',names=col_names)
array = data.values
x = array[:,0:8]
y = array[:,8]
print(x.shape,y.shape)
# 1
# scaler = StandardScaler()
# 2
# scaler = MinMaxScaler(feature_range=(0,1))
# 3
scaler = MinMaxScaler()
rescaled_X = scaler.fit_transform(x)
print(rescaled_X)

model = LinearRegression()
model.fit(x,y)

predicted_Y = model.predict(x)
y = (predicted_Y>0.5).astype(int)
print(y)


