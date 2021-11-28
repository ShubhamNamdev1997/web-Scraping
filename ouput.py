import requests
from bs4 import BeautifulSoup
import csv
import random
import json
Url = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
r = requests.get(Url)
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'class':'product-container'})
outputs = []
for row in table.findAll('div',
                         attrs = {'class':'product'}):
    output = {}
    output['price'] = float(row.find("span", {"class":"price"}).text[1:])
    output['title'] = row.a['title'][19:]
    if row.find("span", {"class":"out-of-stock"}).text == 'Out of Stock':
        output['stock'] = False
    else:
        output['stock'] = True
    output['maftr'] = row.find('a',{"class":"catalog-item-brand"}).text
    outputs.append(output)


filename = 'output.json'
with open(filename, 'w',newline='') as f:
    json.dump(outputs,f)