from numpy.core.records import array
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('linear_regression/home_work/data.txt', delimiter = ',')
x = data[:,0].reshape(-1, 1)
y = data[:,1].reshape(-1, 1)

learning_rate = 0.1
w = [1.2,2.3,321.2]
for j in range(1,1000):
    cost_a = 0
    cost_b = 0
    cost_c = 0
    for i in range(len(x)):
        cost = w[0]*x[i]*x[i] + w[1]*x[i] + w[2]
        cost_a += cost*x[i]*x[i]
        cost_b += cost*x[i]
        cost_c += cost
    w[0] -= cost_a*learning_rate
    w[1] -= cost_b*learning_rate
    w[2] -= cost_c*learning_rate

print(w)
# plt.plot(x,y,'go')
# plt.show()

