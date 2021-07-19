import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
data = np.loadtxt('linear_regression/data.txt', delimiter = ',')

X = data[:,0].reshape(-1, 1)
y = data[:,1].reshape(-1, 1)

# đặt linerRegersion
lrg = LinearRegression()

#cho dữ liệu vào để fix
lrg.fit(X,y)

#tạo ra biến y mới 
y_new = lrg.predict(X)

plt.plot(X,y,'go')
plt.plot(X,y_new)
plt.show()

print(y_new)