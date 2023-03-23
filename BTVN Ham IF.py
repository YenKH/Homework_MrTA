#!/usr/bin/env python
# coding: utf-8

# Bài 1: Nhập vào số tự nhiên (0-6) trả kết quả về thứ 2 - CN

# In[3]:


Num = int(input('Nhập vào một số (trong khoảng 0-6): '))
thu = 'Thứ 2' if Num ==0 else 'Thứ 3' if Num ==1 else 'Thứ 4' if Num ==2 else 'Thứ 5' if Num ==3 else 'Thứ 6' if Num == 4 else 'Thứ 7' if Num ==5 else 'Chủ nhật' if Num ==6 else 'Lỗi nhập dữ liệu đầu vào'
print (thu)


# Bài 2: Phần mềm tính giá tiền điện

# In[4]:


a = float(input('Nhập vào số điện tiêu thụ của bạn: '))
b0 = 1768
b1 = 1734
b2 = 2014
b3 = 2536
b4 = 2834
b5 = 2927
if a<0 : 
    print(f''' Vui lòng nhập lại...
    Số điện tiêu thụ phải >0''')
elif a==0:
    print(f'Số tiền điện phải nộp : 0đ')
else :
    muc0 = 50*b0
    muc1 = muc0 + 50*b1
    muc2 = muc1 + 100*b2
    muc3 = muc2 + 100*b3
    muc4 = muc3 + 100*b4
    tien_dien = a*b0 if a <=50 else muc0+(a-50)*b1 if a<=100 else muc1+(a-100)*b2 if a<=200 else muc2+(a-200)*b3 if a<=300 else muc3 + (a-300)*b4 if a<=400 else muc4 + (a-400)*b5
print (f'Số tiền phải trả:', f'{tien_dien:,}' , 'đ')


# Bài 3: Hiển thị đa thức bậc 2

# In[8]:


a1 = float(input('Nhập hệ số thứ nhất của đa thức: '))
b1 = float(input('Nhập hệ số thứ hai của đa thức: '))
c1 = float(input('Nhập hệ số thứ ba của đa thức: '))
hs1 = '*x^2'
hs2 = '*x'
if a1==0 :
    print(f'Đa thức bậc 2 cần có hệ số thứ nhất khác 0')
else :
    a = '' if a1==1 else '-' if a1 == -1 else str(a1) 
    b="" if b1 ==1 else '-' if b1 == -1 else '+'+ str(b1) if b1>0 else str(b1)
    if b1 == 0 :
        hs2 ==""
    c="" if c1==0 else '+'+ str(c1) if c1>0 else str(c1)
    print (f' Phương trình bậc 2: ' + a + hs1 + b + hs2 + c)


# In[ ]:





# In[ ]:




