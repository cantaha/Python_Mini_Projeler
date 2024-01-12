import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository():
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentuser = {}
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    print(user)
                    user = json.loads(user)
                    new_user = User(username=user["username"], password=user["password"], email=user["email"])
                    self.users.append(new_user)


    def register(self,user: User):
        self.users.append(user)
        self.savetofile()
        print("Kullanıcı Kaydedildi")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentuser = user
                print("Login Başarılı")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentuser = {}
        print("Çıkış Yapıldı")

    def identity(self):
        if self.isLoggedIn:
            print(f"Username {self.currentuser.username}")
        else:
            print("Giriş Yapılmadı")
    def savetofile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json", "w") as file:
            json.dump(list, file) # tekil olan dump metodu ile dosya çalışmaları, çoğul olan dumps metodu yalnızca ile json'a tipine dönüştürme işlemlerini yaparız


repository = UserRepository()

while True:
    print("Menu".center(50, "-"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nSeçiminiz: ")
    if secim == "5": break
    else:
        if secim == "1":
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == "2":
            if repository.isLoggedIn:
                print("Zaten Giriş Yapıldı!")
            else:
                username = input("Username: ")
                password = input("Password: ")
                repository.login(username, password)

        elif secim == "3":
            repository.logout()

        elif secim == "4":
            repository.identity()

        else: print("Yanlış Seçim")
