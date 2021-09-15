def ebob_bulma(x,y):
    i = 1
    ebob = 1
    while(i <= x and i <= y):
        if ( not (x % i) and not (y % i)):
            ebob = i
        i += 1
    return ebob
while True:
    x = int(input("Birinici Sayı:"))
    y = int(input("İkinci Sayı:"))

    print("Ebob:", ebob_bulma(x,y))