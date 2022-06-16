#Imports

import csv
import requests
from bs4 import BeautifulSoup
import datetime


#declaring class for getting csv file

class url_to_csv:
    '''The url_to_csv class is a class using BeautifulSoup for sending requests to Investing.com and gathering data from it about a particular asset'''


    def __init__(self, url:str = None, asset:str = None, export_path:str = None, date_from:str= None, date_to:str = None, cur_id:str = '945629'):
        '''Constructor for the url_to_csv class
        Takes 6 optional arguments:
            1) url: the url of the base site
            2) asset: the name of the stock on investing.com
            3) export_path: the path for the exported csv
            4) date_from: date in DD/MM/YYYY format as the starting date
            5) date_to: date in DD/MM/YYYY format as the ending date
            6) cur_id: ID as seen in the POST tab in Network settings (TESTING REQUIRED)'''

        self.__url         = url
        if url == None:
            self.__url = "https://in.investing.com/instruments/HistoricalDataAjax"
        self.asset       = asset
        self.export_path = export_path
        self.__date_from   = date_from
        if(date_from == None):
            self.__date_from = '01/01/2020'
        self.__date_to     = date_to
        if(date_to == None):
            self.__date_to = datetime.datetime.today().strftime('%d/%m/%Y')
        self.__payload = {'header': self.asset, 
                        'st_date': self.date_from, 
                        'end_date': self.date_to, 
                        'sort_col': 'date', 
                        'action': 'historical_data', 
                        'smlID': '145284', 
                        'sort_ord': 'DESC', 
                        'interval_sec': 'Daily', 
                        'curr_id': cur_id
                        }

    def set_url(self, url:str):
        '''Function for setting url for POST requests
        Arguments:
        1) url: the url to set the url_to_csv object's url to '''

        if(url == None): return
        self.__url = url

    def set_date_range(self, date_from:str = None, date_to:str = None):
        '''Function for setting the date ranges
        Takes two optional arguments:
        1) date_from: starting date
        2) date_to: ending date

        Please note that the date should be in 'DD/MM/YYYY' format
        '''
        if date_from != None:
            self.__date_from = date_from
        if date_to != None: 
            self.__date_to = date_to
    

    def save_data(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
                    'Origin': 'https://www.investing.com',
                    'x-requested-with': 'XMLHttpRequest'}

        r = requests.post(self.__url, 
                        data = self.__payload,
                        headers = headers
                        )
        
        soup = BeautifulSoup(r.content, features = 'html.parser')
        table = soup.find(['table', {'class':'genTbl closedTbl historicalTbl'}])
        #have to find class genTbl closedTbl historicalTbl

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
            if(flag):
                break
            if(len(dictionary.keys()) != 0):
                dict_list.append(dictionary)
            i+=1
        
        self.__write_csv(variables, dict_list)
        print("WRITTEN TO ", self.export_path)
        

    def __write_csv(self, vars, dict):
        with open(self.export_path, 'w') as f:
            w = csv.DictWriter(f, vars)
            w.writeheader()
            for d in dict:
                w.writerow(d)



