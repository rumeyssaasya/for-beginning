print("""
*********
ATM MAKİNESİNE HOŞ GELDİNİZ...

İŞlemler;
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme
PROGRAMDAN ÇIKMAK İÇİN 'q' YA BASINIZ
*********""")

bakiye = 1000

while True:
    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q" ):
        print("Tekrar Bekleriz.")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl'dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Yatırmak İstediğiniz Miktar:"))

        print("Yeni Bakiyeniz {} tl'dir".format(bakiye + miktar))
        bakiye += miktar

    elif (işlem == "3"):
        miktar2 = int(input("Çekmek İstediğiniz Miktar:"))

        if (miktar2 > bakiye):
            print("Bakiyeniz Yetersiz.")
            continue
        print("Kalan Paranız {} tl'dir".format(bakiye - miktar2))
        bakiye -= miktar2
    else:
        print("Geçersiz İşlem.")









