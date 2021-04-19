#url = "https://prnt.sc/1npf96"

from bs4 import BeautifulSoup
import requests
url = requests.get("https://prnt.sc/1npf96")

soup = BeautifulSoup(url.text, "html.parser")
print(soup)