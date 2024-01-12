def dosyalarıOku():
    with open("Sınav_Notları.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(notHesapla(satir))


def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    notlar = liste[1].split("-")
    ogrenciler = liste[0]

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1+not2+not3)/3
    if ort >= 90 and ort <= 100:
        harf = "AA"
    elif ort >=60 and ort <=90:
        harf = "BB"
    elif ort < 60:
        harf = "FF"
    return ogrenciler + ": " + harf + "\n"

def notGir():
    ad = input("Öğrenci İsmi: ")
    soyad = input("Öğrenci Soyismi: ")
    not1 = input("1. Not: ")
    not2 = input("2. Not: ")
    not3 = input("3. Not: ")
    with open("Sınav_Notları.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ": " + not1 + "-" + not2 + "-" + not3 + "\n")
        print("Notlar Kaydedildi")
def notKayit():
    with open("Sınav_Notları.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(notHesapla(i))
        with open("Sınav_Sonuçları", "w", encoding="utf-8") as file2:
            for j in liste:
                file2.write(j)
    print("Notlar Sınav Sonuçları Dosyasına Kaydedildi")

while True:
    print("Menu")
    islem = input("1- Notları Oku\n2- Not Gir\n3- Not Kayıt\n4- Çıkış \n")
    if islem == "1":
        dosyalarıOku()
    elif islem == "2":
        notGir()
    elif islem == "3":
        notKayit()
    elif islem == "4":
        break
    else:
        print("hatalı seçim")