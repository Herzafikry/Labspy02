#labspy02

a = input("Masukkan bilangan A :")
b = input("Masukkan bilangan B :")
c = input("Masukkan bilangan C :")

if a > b and a > c:
    terbesar = a
else:
    if b > c and b > a:
        terbesar = b
    else:
        terbesar = c

print("jadi bilangan terbesarnya adalah : ",terbesar)