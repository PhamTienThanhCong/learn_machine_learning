import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #tạo ma trận 3x4

b = a[:2,1:4] #lấy từ đồ thị ra 2 hàng đầu tiên và từ cột 1 tới cột 4
print(a)
print(b)

#khởi tạo tọa độ xy 
x=np.arange(-10,10,0.1) #khởi tạo 1 mảng từ -10 tới 10 với bước nhảy 0.1  
y1=2*x*x - 5*x + 5
y2=np.sin(x)

plt.subplot(2,1,1) #tạo và vẽ trên đồ thị 1 có kích cỡ 2x1
plt.plot(x,y1) #vẽ đồ thị với x,y
plt.title("do thi 1") #tiêu đề 

plt.subplot(2,1,2) #tạo và vẽ trên đồ thị 2 có kích cỡ 2x1
plt.plot(x,y2) 
plt.title("do thi 2")

# plt.show() #show đồ thị