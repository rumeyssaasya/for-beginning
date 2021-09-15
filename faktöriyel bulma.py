print("""
*****************************
FAKTÖRİYEL BULMA PROGRAMI

Çıkmak İçin q'ya Basınız
*****************************
""")
while True:
    sayı = input("sayı:")
    if sayı == "q":
        print("Tekar Bekleriz.")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            print("faktöriyel",faktoriyel,"i:",i)
            faktoriyel *= i
        print("Faktöriyel",faktoriyel)