print("Progam Mencari Bilangan Terbesar Dari 3 Bilangan")

a = int(input("Masukan Bilangan Pertama :"))
b = int(input("Masukan Bilangan Kedua :"))
c = int(input("Masukan Bilangan Ketiga :"))

if a > b > c:
    print("Bilangan Pertama adalah yang terbesar : %s "%a)
elif b > c:
    print("Bilangan Kedua adalah yang terbesar : %s"%b)
else:
    print("Bilangan Ketiga adalah yang terbesar : %s"%c)
