#hata çözümleme

try:
    sayi = int(input("sayi girin: "))
except (ValueError, ZeroDivisionError):
    print("bir hata oluştu")
    print("tip uyuşmazlığı")
    sayi = int(input("Lütfen sayısal bir değer giriniz"))


if sayi <= 0:
    sayi = int(input("Lütfen pozitif bir sayı giriniz"))
if sayi > 0:
    print("onaylandı")


import sys

liste = [7,'taha',0,3,"6"]

for x in liste:
    try:
        print("sayi: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç: " + str(sonuc))
    except (ValueError,ZeroDivisionError):
        print(str(x) + " Uygun Değil")
        continue
    except:
        print(str(x) + " hesaplanamadı ")
        print("Sistem Hatası: " + str(sys.exc_info()[0]))
    finally:
        print(("işlem bitti"))