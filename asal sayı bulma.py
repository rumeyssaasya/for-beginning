def asal_mi(sayı):
    if (sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if (sayı % i == 0):
                return False
            return True
while True:
    sayı = input("Sayı Giriniz:")
    if (sayı == "q") :
        print("Tekrar Bekleriz....")
        break
    else:
        sayı = int(sayı)

        if (asal_mi(sayı)):
            print("Sayı bir asal sayıdır...")
        else:
            print("Sayı asal bir sayı değildir...")
