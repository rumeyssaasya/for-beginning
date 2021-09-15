print("""
****************
armstrong = 1634 = 1**4 + 6**4 + 3**4 + 4**4
****************""")

while True:

    sayı = input("Sayı:")

    uzunluk = len(sayı)

    toplam = 0

    for i in range(uzunluk):
        toplam = toplam + int(sayı[i]) ** int(uzunluk)

    if (toplam == int(sayı)):
        print("Amstrong.")

    else:
        print("Amstrong Değildir.")


