"""a. Variabel merupakan sebuah nama untuk menyimpan sebuah nilai atau data di dalam program.
b. Variabel yang terdapat pada kode diatas adalah:
• Y2h
• X
• _t
c.Kesalahan:
• Variabel y2h not define 
• di for statement (line 3) kurang “:” diakhirnya
• if x%2 seharusnya menggunakan “==”bukan “=”
• Variabel x di elif tidak boleh 0 karena tidak dapat dihitung, seharusnya menggunakan x! = 0 jadi jika  x = 0 outpunya false

c. Kode yang benar:"""

y2h = float(input ('Masukan nilai untuk variabel y2h = ')) #untuk memasukan nilai untuk variabel y2h
_t = 18 #variabel _t
for x in range (5):
    if x%2 == 1:
        y2h = _t-x
    elif x != 0 and _t>x:
        _t = _t / x
    else:
        y2h = y2h + 1
print (x, y2h)
