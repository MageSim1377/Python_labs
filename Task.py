import requests as req
from bs4 import BeautifulSoup
import lxml
import time
import csv
import string
import sys

f = open(sys.argv[2], 'w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(["country", "city", "area", "population"])

countries = []

with open(sys.argv[1], 'r') as f:
    countries = [line.rstrip() for line in f]

cache = {}

headers = {'User-Agent': 'Chrome/91.0.4472.124'}

with req.Session() as session:
    for country in countries:
        url = f'https://en.wikipedia.org/wiki/{country}'
        soup = ''
        if url in cache.keys():
            soup = cache[url]
        else:
            response = session.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            cache[url] = soup

        for unwanted in soup.find_all('sup'):
            unwanted.extract()

        capital = soup.find('table', class_="infobox ib-country vcard").find('td', class_="infobox-data").find('a').text
        areaInfo = soup.find('table', class_="infobox ib-country vcard").find_all('tr', class_=["mergedrow", "mergedtoprow"])
        #print(areaInfo.find_all('td', class_="infobox-data")[4].text)
        area = ''
        for i in range(len(areaInfo)):
            if 'Area' in areaInfo[i].text:
                area = areaInfo[i + 1].find('td').text.split()[0]
                area = ''.join([el for el in area if el.isdigit() or el == '.'])
                break

        population = ''
        for i in range(len(areaInfo)):
            if 'Population' in areaInfo[i].text:
                population = areaInfo[i + 1].find('td').text.split()[0]
                population = ''.join([el for el in population if el.isdigit() or el == '.'])
                break
            

        print(country, capital, area, population, sep=',')
        writer.writerow([country, capital, area, population])

        time.sleep(3)

f.close()