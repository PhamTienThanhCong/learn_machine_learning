import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression

# nhập dữ liệu data vào từ file csv 
data = pd.read_csv('logistic_regression\data.csv').values
# tách dữ liệu
x = data[:,:2]
y = data[:,2]
# xử lí chọn dự liệu cho vay và không cho vay riêng
x_pain_1 = x[y[:]==1]
x_pain_0 = x[y[:]==0]
# vẽ nó
plt.plot(x_pain_1[:,0],x_pain_1[:,1],'bo')
plt.plot(x_pain_0[:,0],x_pain_0[:,1],'ro')
# khởi tạo Logistic Regression
lgr = LogisticRegression()
# fit dữ liệu
lgr.fit(x,y)
# dùng predict để dự đoán giá trị
x_test = [[5,2],[3,1],[10,0.5]]
print(lgr.predict(x_test))

plt.show()