import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.root.cz")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text,"html.parser");
print(soup.title)
print(soup.title.text)
