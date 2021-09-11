from numpy.core.records import array
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = np.loadtxt('linear_regression/home_work/data.txt', delimiter = ',')
x = data[:,0].reshape(-1, 1)
y = data[:,1].reshape(-1, 1)

lrg = LinearRegression()
lrg.fit(x,y)

y_new = lrg.predict(x)

plt.plot(x,y,'go')
plt.plot(x,y_new,'yo')

plt.show()