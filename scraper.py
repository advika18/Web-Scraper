#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:03:17 2020

@author: advikabattini
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Data-science-intern&where=Seattle__2C-WA'
page = requests.get(url)
#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find(id='ResultsContainer')
print(results.prettify())

filt = results.find_all('section',class_='card-content')
for i in filt:
    title = i.find('h2', class_='title')
    link = i.find('a')
    company = i.find('div', class_='company')
    location = i.find('div', class_='location')
    if None in (title,company,location,link):
        continue
    print(f'title: {title.text.strip()}, link:{link["href"]}, company: {company.text.strip()}, location: {location.text.strip()}\n')
    
    
interested_jobs = results.find_all('h2',class_='title',text=lambda x: "science" in x.lower())
print(len(interested_jobs))
for i in interested_jobs:
    link = i.find('a')
#    if None in (title,company,location):
#        continue
    print(f'title: {i.text}, link:{link["href"]} \n')
    