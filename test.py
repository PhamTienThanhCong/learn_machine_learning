mssv  = int(input("nhập mssv: "))
mod_a = int(input("nhập số a chia: "))
mod_b = int(input("nhập số b chia: "))

Tong = 0
a = 0
b = 0
c = 0
for i in range(1,mssv+1):
    if i%mod_a==0 or i%mod_b==0:
        Tong+=1
    if i%mod_a==0:
        if i%mod_b==0:
            if c==0:
                print("Bội Chung:",i)
            c+=1
        a+=1
    if i%mod_b==0:
        b+=1
print("Tổng các số chia hết cho a: ",a)
print("Tổng các số chia hết cho b: ",b)
print("Tổng số chia hết cho bội chung: ",c)
print("Tổng số a+b: ",a+b)
print("kết quả: ",Tong)