import numpy as np
import matplotlib.pyplot as plt
#numOfPoint = 30
#noise = np.random.normal(0,1,numOfPoint).reshape(-1,1)
#x = np.linspace(30, 100, numOfPoint).reshape(-1,1)
#N = x.shape[0]
#y = 15*x + 8 + 20*noise
#plt.scatter(x, y)

data = np.loadtxt('learning_beginer/data.txt', delimiter = ',')
N = data.shape[0]
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)
plt.scatter(x, y)
plt.xlabel('mét vuông')
plt.ylabel('giá')

x = np.hstack((np.ones((N, 1)), x))

w = np.array([0.,1.]).reshape(-1,1)

numOfIteration = 100
cost = np.zeros((numOfIteration,1))

learning_rate = 0.000001
for i in range(1, numOfIteration):
    r = np.dot(x, w) - y
    # cost[i] = 0.5*np.sum(r*r)
    w0_train = 0.0
    w1_train = 0.0
    w[0] -= learning_rate*np.sum(r)
    # correct the shape dimension
    w[1] -= learning_rate*np.sum(np.multiply(r, x[:,1].reshape(-1,1)))
    # w[1] -= learning_rate*np.sum()
    # print(cost[i])
    # for i in range(len(x)):
    #     w0_train += w[1]*x[i][1]+w[0]-y[i]
    #     w1_train += (w[1]*x[i][1]+w[0]-y[i])*x[i][1]
    # w[0] -= learning_rate*w0_train
    # w[1] -= learning_rate*w1_train
print(w[0],w[1])
#predict = np.dot(x, w)
#plt.plot((x[0][1], x[N-1][1]),(predict[0], predict[N-1]), 'r')
# plt.show()

# y1 = w[1]*x[:,1] + w[0]

# plt.plot(x[:,1],y1)

# plt.show()
# x1 = 50
# y1 = w[0] + w[1] * 50
# print('Giá nhà cho 50m^2 là : ', y1)