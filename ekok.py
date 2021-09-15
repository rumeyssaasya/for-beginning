def ekok_bulma(x,y):
    i = 2
    ekok = 1
    while True:
        if(x % i == 0 and y % i ==0):
            ekok *=i

            x //= i
            y //= i

        elif(x % i == 0 and y % i != 0):
            ekok *= i

            x //= i

        elif(x % i != 0 and y % i == 0):
            y //= i
        else:
            i += 1
        if(x == 1 and y == 1):
            break
    return ekok
while True:
    x = int(input("Birinci Sayı:"))
    y = int(input("İkinci Sayı:"))
    print("Ekok:",ekok_bulma(x,y))