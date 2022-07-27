import random
import time

rastgelesayı=random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("Tahmininiz:"))
    if(tahmin<rastgelesayı):
        print("Bilgilar sorgulanıyor..")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyiniz...")

        tahmin_hakki-=1
    elif (tahmin > rastgelesayı):
        print("Bilgilar sorgulanıyor..")
        time.sleep(1)
        print("Daha küçük bir sayı söyleyiniz...")
        tahmin_hakki -= 1
    else:
        print("Doğru Tahmin. Tebrikler...")
        print("Yeniden oynamak için 1'e, çıkmak için 2'ye basınız.")
        break
    if(tahmin_hakki==0):
        print("Tahmin hakkınız bitmiştir..")
        print("Belirlenen sayı:",rastgelesayı)

