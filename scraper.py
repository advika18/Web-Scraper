#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:03:17 2020

@author: advikabattini
"""

import requests
from bs4 import BeautifulSoup


class Monster:
    def __init__(self, url='https://www.monster.com/jobs/search/?q=Data-science-intern&where=Seattle__2C-WA'):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.results = self.soup.find(id='ResultsContainer')
              
    def __str__(self):
        return self.results.prettify()
    
    def all_jobs(self):
        filt = self.results.find_all('section',class_='card-content')
        for i in filt:
            title = i.find('h2', class_='title')
            link = i.find('a')
            company = i.find('div', class_='company')
            location = i.find('div', class_='location')
            if None in (title,company,location,link):
                continue
            print(f'title: {title.text.strip()}, link:{link["href"]}, company: {company.text.strip()}, location: {location.text.strip()}\n')
         
    def filtered_jobs(self, word='science'):
        interested_jobs = self.results.find_all('h2',class_='title',text=lambda x: word in x.lower())
        print(len(interested_jobs))
        for i in interested_jobs:
            link = i.find('a')
        #    if None in (title,company,location):
        #        continue
            print(f'title: {i.text}, link:{link["href"]} \n')


class Indeed:
    def __init__(self, url='https://www.indeed.com/jobs?q=data+science&l=Seattle%2C+WA'):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.results = self.soup.find(id='resultsCol')
              
    def __str__(self):
        return self.results.prettify()
    
    def all_jobs(self):
        filt = self.results.find_all('div',class_='jobsearch-SerpJobCard unifiedRow row result')
        for i in filt:
            title = i.find('div', class_="title")
            link = i.find('a')
            company = i.find('span', class_="company")
            location = i.find('div', class_="location accessible-contrast-color-location")
            if location == None:
                location = i.find('span', class_="location accessible-contrast-color-location")    
            if None in (title,company,location,link):
                continue
            print(f'title: {title.text.strip()}, link:{link["href"]}, company: {company.text.strip()}, location: {location.text.strip()}\n')

    def filtered_jobs(self, word='science'):
        interested_jobs = self.results.find_all('div',class_='title',text=lambda x: word in x.lower())
        print(len(interested_jobs))
        for i in interested_jobs:
            link = i.find('a')
        #    if None in (title,company,location):
        #        continue
            print(f'title: {i.text}, link:{link["href"]} \n')



            
            
temp = Indeed()
print(temp) 
temp.all_jobs() 
temp.filtered_jobs()           
            
            
                
"""
url = 'https://www.indeed.com/jobs?q=data+science&l=Seattle%2C+WA'
page = requests.get(url)
#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find(id='resultsCol')
print(soup.prettify())

filt = results.find_all('div',class_='jobsearch-SerpJobCard unifiedRow row result')
for i in filt:
    title = i.find('div', class_="title")
    link = i.find('a')
    company = i.find('span', class_="company")
    location = i.find('div', class_="location accessible-contrast-color-location")
    if location == None:
        location = i.find('span', class_="location accessible-contrast-color-location")    
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
"""   