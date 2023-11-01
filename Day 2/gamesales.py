pip install requests
pip3 install beautifulsoup4 

import requests
from bs4 import BeautifulSoup

def get_steam_sales():
    url = "https://store.steampowered.com/search/?specials=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        games = soup.find_all("a", {"class": "search_result_row"})

        for game in games:
            title = game.find("span", {"class": "title"}).text
            original_price = game.find("div", {"class": "search_price"}).text.strip()
            discount_price = game.find("div", {"class": "search_discount"}).text.strip()

            print(f"Title: {title}")
            print(f"Original Price: {original_price}")
            print(f"Discount Price: {discount_price}\n")
    else:
        print("Failed to fetch Steam sale data.")

if name == "main":
    get_steam_sales()