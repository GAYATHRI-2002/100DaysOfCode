import requests
from bs4 import BeautifulSoup

# 1. Get user input
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

# 2. Correctly format the URL
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# 3. Use headers to prevent a 403 Forbidden Error
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(url=url, headers=header)
response.raise_for_status()  # Optional: Raises an error if the request failed

soup = BeautifulSoup(response.text, "html.parser")

# 4. Use a more reliable selector targeting the title ID attribute
song_titles_tags = soup.find_all("h3", id="title-of-a-story")

# 5. Extract and clean the text
song_names = [song.getText().strip() for song in song_titles_tags]

print(song_names)