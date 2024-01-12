# regex modülü (regular expressions)

import re

ornek = "base42"
patern = r"base\d+"
print(re.search(patern, ornek))
#backslash \ ve d harfi regex modulü içerisinde rakamları ifade eder

cumle2 = "telefon numaram 0555-7946131"
patern2 = r"\d{3,4}-\d{7}"
eslesme = re.search(patern2, cumle2)
print(eslesme.group())

#sonuc= re.search(patern2, cumle2)
#print(sonuc.span())
print(re.search(patern2, cumle2))

ornek2 = "yeni telefon no 5555441122"
patern3 = r"\d{4}"
#sonuc2 = re.search(patern3, ornek2)
#print(sonuc2.span())
print(re.search(patern3, ornek2))

ornek4 = "komutu oluşturmuş olduğun ve içine yazmış olduğun dosyanın tüm istatistiki 'bilgi54' bilgilerini verir. "
patern4 = r"\s\w{6,}" #virgül ile verilen komutlarda virgülden sonrası " 'den daha fazla" anlamında kullanılır. \s ifadesi space olarak kullanılır.
#\w her değer için kullanılır.
patern5 = r"\d?" #soru işareti ya 1 ya da hiç anlamında kullanılır.
patern6 = r"\w*\d+" # + işareti de en az bir rakam anlamına gelir. * kullanımı ise yine en az bir ifade anlamına gelir.

for i in re.finditer(patern4, ornek4):
    print(i.group(), i.span())

#for i in re.finditer(patern5, ornek4):
#    print(i.group(), i. span())

for i in re.finditer(patern6, ornek4):
    print(i.group(), i.span())

def gsmOperatorleriniBul(telNo):
    patern = r"(\d{3})-(\d{7})"
    eslesme = re.search(patern, telNo)
    if eslesme:
        try:
            gsmKod = eslesme.group(1)
            if gsmKod.startswith("54"):
                print("Vodafone")
            elif gsmKod.startswith("501") or gsmKod.startswith("505") or gsmKod.startswith("506") or gsmKod.startswith("555"):
                print("Avea")
            elif gsmKod.startswith("53"):
                print("Turkcell")
            else:
                print("Şebeke Bulunamadı")
        finally:
            print(eslesme.group())
    else:
        print("Patern bulunamadı!")

telNo = "telefon numaram 0555-7946131"
gsmOperatorleriniBul(telNo)
