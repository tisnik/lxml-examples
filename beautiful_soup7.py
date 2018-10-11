import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

response = requests.get("https://www.root.cz/clanky/zaklady-pouziti-rezimu-org-mode-v-emacsu/")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

for p in soup.find_all("strong"):
    print(p.text)

print("\n\n\nTables")

for table in soup.find_all("table"):
    for tr in table.find_all("tr"):
        for item in tr.find_all(["th", "td"]):
            print(item.text + "\t|\t", end="")
        print()
    print("-------------------")
