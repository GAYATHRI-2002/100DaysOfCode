from bs4 import BeautifulSoup
import requests


date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

response =requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.find_all(name="h3", class_="chart-entry__title")
songs = [i.getText().strip() for i in all_songs]
print(songs)