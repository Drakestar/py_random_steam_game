from bs4 import BeautifulSoup
import requests

url2 = "http://steamcommunity.com/profiles/76561198043794238/games/?tab=all"
url = "https://steamcommunity.com/id/jaccat239/games/?tab=all"
page = requests.get(url2)
soup = BeautifulSoup(page.content, 'html.parser')

person = {}
#letters = soup.find_all("gameListRowItemName")
pretty_text = soup.prettify()

file = open("grossgames.txt", "w")
#letters = soup.find_all(class_='gameListRowItemName')
for lines in pretty_text.splitlines():
    if "rgGames" in lines:
        file.write(lines)
file.close()
