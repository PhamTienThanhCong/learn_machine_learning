from operator import le
import re
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import hstack

data = np.loadtxt('learning_beginer/data.txt', delimiter = ',')

x = data[:,0].reshape(-1, 1)
y = data[:,1].reshape(-1, 1)

plt.plot(x,y,'go')

x_train = np.hstack((np.ones((len(x),1)),x))
w = np.array([[1.1],[1.1]])

learning_rate = 0.000001
cost_his = []

for i in range(0,1000):
    cost = np.dot(x_train,w) - y
    cost_his.append(0.5*np.sum(cost*cost))
    w[0] -= learning_rate*np.sum(cost)
    w[1] -= learning_rate*np.sum(np.multiply(cost, x_train[:,1].reshape(-1,1)))

# print(cost_his)
print('gia tri a,b ')
print(w)
y2 = w[0] + w[1]*x
plt.plot (x,y2)

plt.show()
