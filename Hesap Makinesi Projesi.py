from tkinter import *

master = Tk()
master.title("Hesap Makinesi")
master.geometry("250x300")

sayi2 = 0
def hesapla():
    global sayi2
    sayi2 = float(islemFrame.get())
    print(sayi2)
    global hesap
    sonuc = 0
    if(hesap==0):
        sonuc = sayi1 + sayi2
    elif(hesap==1):
        sonuc = sayi1 - sayi2
    elif(hesap==2):
        sonuc = sayi1 / sayi2
    elif(hesap==3):
        sonuc = sayi1 * sayi2
    islemFrame.delete(0, "end")
    islemFrame.insert(0, str(sonuc))

def temizle():
    islemFrame.delete(0,"end")
def yaz(x):
    s = len(islemFrame.get())
    islemFrame.insert(s, str(x))
    #print(x)

hesap = 5
sayi1 = 0
def islemler(x):
    global hesap
    hesap = x
    global sayi1
    sayi1 = float(islemFrame.get())
    print(hesap)
    print(sayi1)
    islemFrame.delete(0,"end")

islemFrame = Entry(font="Verdana 14 bold", width=17, justify=RIGHT)
islemFrame.place(x=25, y=20)

b = []
sayac = 0

for i in range(1,10):
    b.append(Button(text=str(i), font="Verdana 14 bold", command= lambda x=i:yaz(x)))

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50, y=50+i*50)
        sayac += 1

islem = []

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i:islemler(x)))

sifirButonu = Button(text=0, font="Verdana 14 bold", command= lambda x=0:yaz(x))
sifirButonu.place(x=20, y=200)

noktaButonu = Button(text=".", font="Verdana 14 bold", width=1, command= lambda x=".":yaz(x))
noktaButonu.place(x=70, y=200)

esittirButonu = Button(text="=", font="Verdana 14 bold", width=1, foreground="orange", command= hesapla)
esittirButonu.place(x=120, y=200)

acButonu = Button(text="AC", font="Verdana 14 bold", width=5, foreground="red", command=temizle)
acButonu.place(x=75, y=240)

islem[0]["text"] = "+"
islem[1]["text"] = "-"
islem[2]["text"] = "/"
islem[3]["text"] = "*"

for i in range(0,4):
    islem[i].place(x=170, y=50+50*i)


master.mainloop()