#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = 'https://www.skolmaten.se/hagbyskolan/'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', class_="week visible")

print(f"{div.get_text()}")
