def tambölenleribulma(sayı):
    tam_bölenler = []

    for i in range(2,sayı):
        if(sayı % i == 0):
            tam_bölenler.append(i)
    return tam_bölenler

while True:
    sayı = input("Sayı Giriniz:")
    if (sayı == "q"):
        print("İyi Günler...")
        break
    else:
        sayı = int(sayı)
        print("Tam bölenler:",tambölenleribulma(sayı))
