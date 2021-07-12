import numpy as np
import matplotlib.pyplot as plt

# Bài toán tìm giá trị nhỏ nhất của hàm số f(x)=x^2+2x+5

# Tạo Giá trị x ngẫu nhiên
x_train = 10
# Tốc độ học tập(độ chuẩn xác)
learning_rate = 0.01
# Số lần học tập và cải thiện
NumOfInteration = 2000

for i in range(0, NumOfInteration):
    cost = 2*x_train + 2 #Tính Giá trị nguyên hàm của hàm số
    x_train -= learning_rate*cost # Tính toán giá trị rồi rút gọn dần

plt.title("Giá Trị Nhỏ nhất của x^2+2x+5") #tiêu đề 
# Tạo một mảng x từ x-10 tới x+10 với bước nhảy là 0.1
x = np.arange(x_train-10,x_train+10,0.1) 
y = x**2 + 2*x +5
plt.plot(x,y)

y_train = x_train**2 + 2*x_train +5
plt.plot(x_train, y_train, 'go')
plt.xlabel(['x = '+str(x_train)])
plt.ylabel(['y = '+str(y_train)])

plt.show()