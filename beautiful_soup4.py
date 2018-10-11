vmport requests
from bs4 import BeautifulSoup

response = requests.get("https://pypi.python.org/simple/")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

for a in soup.find_all("a"):
    print(a.text)
