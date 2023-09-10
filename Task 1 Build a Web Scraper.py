# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:16:31 2023

@author: hp
"""

import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com"

response=requests.get(url)

if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    quotes=soup.find_all('span',class_='text')
    authors=soup.find_all('small',class_='author')
    for i in range(len(quotes)):
        print(f"Quotes: {quotes[i].text}")
        print(f"Authors: {authors[i].text}")
        print()
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    
    
