from operator import le
import re
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import hstack

# Dộc dữ liệu từ tệp về ngắn cách nhau bới ","
data = np.loadtxt('linear_regression/data.txt', delimiter = ',')

# Xây dựng chỉnh sửa data x lấy hàng 0 y lấy hàng 1 tạo thành vector 
x = data[:,0].reshape(-1, 1)
y = data[:,1].reshape(-1, 1)

# số lần học và tốc độ học tốc độ càng thấp càng chuẩn nhưng số lần học lại tăng
number_learn = 1000
learning_rate = 0.00001

# cách 1 sử dụng ma trận
def linear_regression_1(a,b,x,y,learning_rate,number_learn):
    #xây dựng lại x thành ma trận nx2 với x[:,0] =1
    x_train = np.hstack((np.ones((len(x),1)),x))
    #xây dựng vector w với w[1]=a và w[0]=b
    w = np.array([[b],[a]])
    # cost_his = [] # tạo mảng lưu trữ hàm mất mát 
    for i in range(0,number_learn):
        # Sử dụng hàm nhân ma trận dot (w[0]*X[:,0] và w[1]*X[:,1])
        cost = np.dot(x_train,w) - y #phép tính tương đương ax + b -y
        # cost_his.append(0.5*np.sum(cost)/len(x)) # lưu giá trị vào mảng loss function
        #tính toán w[0] và w[1] sao cho chuẩn nhất
        #sử dụng gradient với công thức x=x-learning_rate*f'(x)
        # ta có f(w0,w1)=0.5*sum(w0+w1*xi-yi)^2 với i= 1--> n
        w[0] -= learning_rate*np.sum(cost) #f'(x)=w0+w1*xi-yi
        #f'(x)=xi(w0+w1*xi-yi)
        #dùng nultiply để nhân x[:,1] với từng giá trị của mảng cost
        w[1] -= learning_rate*np.sum(np.multiply(cost, x_train[:,1].reshape(-1,1))) 
    return w[1],w[0]

# cách 2 code trâu
def linear_regression_2(a,b,x,y,learning_rate,number_learn):
    # cost_his = [] # tạo mảng lưu trữ hàm mất mát 
    for j in range(number_learn):
        # xây dựng luôn f'(a,b) = 0
        a_train=0 
        b_train=0
        # Tính toán f'(a,b)
        for i in range(len(x)):
            b_train += a*x[i] + b - y[i] # f'(x)=axi +b - yi
            a_train += x[i]*(a*x[i] + b - y[i]) # f'(x)=xi(axi +b - yi)
        # theo công thức nhân với learing rate 
        # x = x-learning_rate*f'(x)
        a -= learning_rate*a_train
        b -= learning_rate*b_train
        # cost_his.append((b_train)*0.5/len(x)) # lưu giá trị vào mảng loss function
    return a,b

a1,b1 = linear_regression_1(0.0,0.0,x,y,learning_rate,number_learn)
a2,b2 = linear_regression_2(1.1,1.1,x,y,learning_rate,number_learn)
print(a1,b1)
print(a2,b2)

# Tính toán y = ax+b với 2 trương hợp a,b khác nhau
plt.subplot(2,1,1)
plt.title('trường hợp 1')
plt.plot(x,y,'go')
y_show = a1*x + b1
plt.plot (x,y_show)

plt.subplot(2,1,2)
plt.title('trường hợp 2')
plt.plot(x,y,'go')
y_show = a2*x + b2
plt.plot (x,y_show)

plt.show()

np.save('linear_regression/new_data.txt',y_show)
