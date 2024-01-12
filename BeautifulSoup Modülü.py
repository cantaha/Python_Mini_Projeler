#BeautifulSoup Modülü
#TODO Aşağıdaki kodları önce commentle sonra teker teker çalış ya da tekrar et!

from bs4 import BeautifulSoup

html_doc = """  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, inital-sclae=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Html Deneme</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <div class="grup1">
        <h2>
        Programlama
        </h2>
        <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
        Modüller
        </h2>
        <ul>
        <li>Menu 1</li>
        <li>Menu 2</li>
        <li>Menu 3</li>
        <li>Menu 4</li>
        </ul>
    </div>
    <img src="bamboo-digital-paper-4708017_1920.jpg" alt="">
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print(soup.prettify()) #beautifulsoup kütüphanesinin html kodlarını düzenleme işlemini yapar prettify komutu. Indentation hatalarını düzenliyor ve kodu olması gerektiği gibi yazıyor.
print(soup.head)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.h1) #talepleri tekrar çalıştır bak. Hepsi html kodlarının doğrudan ilgili kısmını çağırıyor.
print(soup.h2) #sayfada 1'den fazla h2 olduğundan bu metot ile yalnızca bulduğu ilk h2'yi ekrana yazdırır.

result = soup.find_all("h2") #fakat buradaki gibi find_all komutu ile bütün h2'ler ekrana yazdırılabilir.
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]#bu şekilde index olarak da ekrana yazdırılabilir.
print(result)

result2 = soup.div
print(result2)

print(soup.find_all("div")[0])
print(soup.find_all("div")[1].ul)
print(soup.find_all("div")[1].ul.li)#bu şekilde örnek olarak div kısmının 2. indexinin ul etiketinin li etiketine kadar hatta onun içinden istediğimiz sıradakini bile ekrana yazdırabiliriz.
print(soup.find_all("div")[1].ul.find_all("li")) #find_all kullanımı tekrar kullanılabilir
print(soup.find_all("div")[1].ul.find_all("li")[1])

result3 = soup.div.findChildren #buradaki findChildren metodu ise belirtilen etiketin (örnekteki 'div') altındaki tüm etiketleri ekrana yazdırır
print(result3)

print(soup.div)# yalnızca ilk div ekrana yazdırıldı.
print(soup.div.findNextSibling())# üstteki kod çalıştırıldığında gelen ilk div etiketi baz alınarak "findNextSibling" komutu kullanarak bir sonraki etikete geçip ekrana yazdırabiliriz.
print(soup.div.findNextSibling().findNextSibling())# bu şekilde de kullanılabilir

result = soup.find_all("a")
for link in result:
    print(link["href"])