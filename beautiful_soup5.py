import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

response = requests.get("https://pypi.python.org/simple/")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

for a in soup.find_all("a")[:10]:
    package_name = a.text

    url = urljoin("https://pypi.python.org/pypi/project", package_name)
    response = requests.get(url)

    if response.status_code != 200:
        print("Chyba při přístupu na stránku: ", response.status_code)

    package_soup = BeautifulSoup(response.text, "lxml")
    meta_keywords = package_soup.find_all("p", attrs={"class": "tags"})
    if len(meta_keywords) < 1:
        print("Failed to parse and find keywords for '{p}'".format(p=package_name))
        continue

    print(meta_keywords)
