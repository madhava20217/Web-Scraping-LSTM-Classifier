from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.investing.com/commodities/gold-historical-data"

r = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find(['table', {'class':'genTbl closedTbl historicalTbl'}])
table = table.find_next('table')

i = 0
prices = []

dict_list = []

variables = []

for row in table.find_all_next(['tr']):
    dictionary = {}

    j = 0

    flag = False

    for td in row:
        if(i == 0):
            variables.append(td.text)
        else:
            if("Highest:" in td.text): 
                flag = True
                break
            dictionary[variables[j]] = td.text
            j+=1
    if(flag): break

    if(len(dictionary.keys()) != 0):
        dict_list.append(dictionary)

    i+=1

with open('../datasets/gold.csv', 'w') as f:
    w = csv.DictWriter(f, variables)
    w.writeheader()
    for d in dict_list:
        w.writerow(d)