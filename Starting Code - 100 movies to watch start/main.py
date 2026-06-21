import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html,"html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("movies.txt", mode="w",encoding="utf-8") as file:
    for i in movies:
        file.write(f"{i}\n")