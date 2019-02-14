#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

response = requests.get("https://pypi.python.org/simple/")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

for a in soup.find_all("a")[:20]:
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

    print("Keywords for package '{p}'".format(p=package_name))
    keywords_spans = meta_keywords[0].find_all("span", attrs={"class": "package-keyword"})
    for span in keywords_spans:
        for word in span.contents:
            print([k.strip().lower() for k in word.split(",") if k.strip() != ""])
