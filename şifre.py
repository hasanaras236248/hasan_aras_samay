import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int (input("şifreniz kaç karakter olsun"))
sifre = ""
for i in range(sayi):
    sifre += random.choice(karakterler)
print("sifreniz", sifre)
