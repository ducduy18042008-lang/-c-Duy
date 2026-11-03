#Bài 1: Nhập vào số nguyên n, in ra màn hình số gấp đôi của n 
n =int(input())
print(2*n)

#Bài 2 
import math
a = int(input("chieu rong: "))
b = int(input("chieu dai: "))
if a < b : 
    S = a*b - math.pi * ((a/2)**2)
    print ('%.2f'%S)
else: 
    print("khong thoa man dieu kien")

#Bai 3:
c = input("Nhap mot ky tu: ")
if c.isupper():
    print (c.lower())
else:
    print(c.upper())

#Bài 4
n = input("nhap mot chu cai: ")
if n.isalpha():
    print("{c} la ki tu alphabet")
else: 
    print("{c} khong phai la ki tu alphabet")
#Bài 5
c = input("Nhập chữ cái hoa: ") 
if c == 'A':
    print('z')
else:
    print(chr(ord(c) + 31)) # chữ hoa B có mã 66, chữ thường a có 97, nên từ thường lên thành hoa khoảng cách là 31
                            # ord() trả về mã số của kí tự được điền vào
                            # chr() dùng để chuyển một mã số unicode thành ký tự tương ứng
#Bài 6
import math
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a+c>b and b+c > a: 
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)
else: 
    print("khong phai 3 canh cua tam giac")
#Bài 7
#trong python, chỉ số của chuỗi bắt đầu từ 0, chứ không phải từ 1
n = str(input()) # không cần thêm str vì ban đầu máy đã tự động input() chuyển thành chuỗi
print (n[4])     # n[i] là kí tự thứ i+1
print(n[8])
#Bài 8:
name = input("Ten chu ho: ")
old = int(input("Chi so thang truoc: "))
new = int(input("Chi so thang nay: "))

# Tinh so dien tieu thu
n = new - old

# Tinh tien dien
total = 0

if n <= 50:
    total = n * 1984

elif n <= 100:
    total = 50 * 1984 + (n - 50) * 2050

elif n <= 200:
    total = 50 * 1984 + 50 * 2050 + (n - 100) * 2380

elif n <= 300:
    total = 50 * 1984 + 50 * 2050 + 100 * 2380 + (n - 200) * 2998

elif n <= 400:
    total = (50 * 1984 + 50 * 2050 + 100 * 2380
             + 100 * 2998 + (n - 300) * 3350)

else:
    total = (50 * 1984 + 50 * 2050 + 100 * 2380
             + 100 * 2998 + 100 * 3350 + (n - 400) * 3460)

# Cong VAT 8%
total = round(total * 1.08)

print("Ho va ten:", name)
print("Tien phai tra la:", total)
