from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.investing.com/commodities/aluminum-historical-data"

r = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(r.content, 'html')

table = soup.find(['table', {'class':'genTbl closedTbl historicalTbl'}])
table = table.find_next('table')

i = 0
prices = []

dict_list = []

variables = []

for row in table.find_all_next(['tr']):
    # if(i%6 == 0):
    #     price.append

    dictionary = {}

    j = 0

    for td in row:
        if(i == 0):
            variables.append(td.text)
        else:
            print(td.text)
            dictionary[variables[j]] = td.text
            j+=1
    if(len(dictionary.keys()) != 0):
        dict_list.append(dictionary)

    i+=1

with open('../datasets/aluminium.csv', 'w') as f:
    w = csv.DictWriter(f, variables)
    w.writeheader()
    for d in dict_list:
        w.writerow(d)