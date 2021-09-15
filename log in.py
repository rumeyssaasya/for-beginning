print("""**********
Kullanıcı Girişi
**********
""")

sys_kullanıcı_adı = "gamzetheloser"
sys_parola = "zürafa"

giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
        print("Parola Hatalı...")
        giriş_hakkı -=1
    elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı -=1
    elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giriş_hakkı -=1

    else:
        print("Programa Hoş Geldiniz...")
    if (giriş_hakkı == 0):
        print("Giriş Hakkınız Bitmiştir")
        break