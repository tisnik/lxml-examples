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

response = requests.get("https://www.root.cz")

if response.status_code != 200:
    print("Chyba při přístupu na stránku: ", response.status_code)

soup = BeautifulSoup(response.text,"html.parser");
print(soup.title)
print(soup.title.text)
