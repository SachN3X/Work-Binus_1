def terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Masukkan tiga bilangan:")
a = int(input("Bilangan pertama: "))
b = int(input("Bilangan kedua: "))
c = int(input("Bilangan ketiga: "))
print("Bilangan terbesar adalah:", terbesar(a, b, c))
