# Giải phương trình bậc 2: ax^2 + bx + c = 0
a = int(input('nhập a:'))
b = int(input('nhập b:'))
c = int(input('nhập c:'))

denta = b*b - 4*a*c

# Kiểm tra điều kiện và thực thi khối lệnh if nếu điều kiện đúng
if denta < 0:
   print('Phương trình vô nghiệm')

# Nếu điều kiện sai, khối lệnh của else sẽ được thực hiện
elif denta == 0:
   x = -b/(2*a)
   print(' Phương trình có nghiệm kép x =', x)

# Nếu tất cả các điều kiện đều sai nó sẽ thực thi khối lệnh của else
else :
    x1 = (-b-denta**(1/2)) / (2*a)
    x2 = (-b+denta**(1/2)) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt x1= ", x1, ",x2 = ", x2)
