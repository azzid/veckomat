#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = 'https://www.skolmaten.se/hagbyskolan/'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', class_="week visible")

lines = [ x for x in div.get_text().split('\n') 
          if not (
            x == '' or
            x == 'Mån' or
            x == 'Tis' or
            x == 'Ons' or
            x == 'Tor' or
            x == 'Fre'
          )
        ]

mon_i = lines.index('Måndag')
tue_i = lines.index('Tisdag')
wed_i = lines.index('Onsdag')
thu_i = lines.index('Torsdag')
fri_i = lines.index('Fredag')

print(f"{lines[mon_i:tue_i]}")
