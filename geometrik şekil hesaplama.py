print("""Dörtgen için 1; Üçgen için 2 sayısını giriniz...""")


girdi = input("Hangi Geometrik Şekil:")


if girdi == "1":
    b = int(input("Birinci kenar uzunluğu:"))
    c = int(input("İkinci kenar uzunluğu:"))
    d = int(input("Üçüncü kenar uzunluğu:"))
    e = int(input("Dördüncü kenar uzunluğu:"))

    if (b != c != d != e):
       print("Sıradan Dörtgen")

    elif (b == d)!=(c == e):
        print("Dikdörtgen")

    elif (e == b == c == d):
        print("Kare")

    else:
        print("Sıradan Dörtgen")


elif girdi == "2":
    x = int(input("Birinci kenar uzunluğu:"))
    y = int(input("İkinci Kenar uzunluğu:"))
    z = int(input("Üçüncü kenar uzunluğu:"))

    if ((abs(x - y) < z and abs(x + y) < z) or ((z-y)<x and (z+y)<x) or ((x+z)<y and (x-z)<y)):

       if (x == y and y != z) or (x==z and z!=y) or (z==y and y!=x):
        print("İkizkenar Üçgen")

    elif x==y==z:
        print("Eşkenar Üçgen")

    elif x!=y!=z:
        print("Çeşitkenar Üçgen")

    else:
        print("Üçgen Belirtmiyor")