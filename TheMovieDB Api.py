import json
import requests


class theMovieDB:
    def __init__(self):
        self.url = "https://api.themoviedb.org/3/"
        self.key = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZTVmZGE0MGUzMjU5NDEwMTAyYzQxZTBkYzU2Nzc2YyIsInN1YiI6IjY1OTcxMDU1YTY5OGNmNDYxMTQzYTBhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZBdZ5Adcc_jKDOMY24QIidpuvomIrTeLZxITW_UtAEo"
        }

    def getPopulars(self):
        responce = requests.get(self.url+"movie/popular?language=en-US&page=1", headers=self.key)
        return responce.json()

    def searchMovie(self, query, page):
        self.query = query
        self.page = page
        responce = requests.get(self.url+f"search/movie?query={self.query}&include_adult=false&page={self.page}", headers=self.key)
        return responce.json()



movie = theMovieDB()
while True:
    secim = input("1- Popular Movies\n2- Search Movie\n3- Exit\nSeçim: ")
    if secim == "3": break
    elif secim == "1":
        result = movie.getPopulars()
        for i in result['results']:
            print(i['title'])
    elif secim == "2":
        query = input("Arama kelimesi: ")
        page = int(input("Sayfa No: "))
        result = movie.searchMovie(query, page)
        for i in result["results"]:
            print(i["original_title"])


