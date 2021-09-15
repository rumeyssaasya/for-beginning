b = float(input("Kullanıcının Boyu:"))
a = int(input("Kullanıcının Kilosu:"))

print("{} / ({} * {}) = {} ".format(a,b,b,a / (b * b)))


if (18.5 > a / (b * b)):
    print("Zayıf")

elif (18.5 < a / (b * b) <= 25):
    print("Normal")

elif (25 < a / (b * b) <= 30):
    print("Fazla Kilolu")

elif (30 < a / (b * b)):
    print("Obez")