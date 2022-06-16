#Imports
from url_to_csv.scraper import *
from os.path import dirname, abspath, join

path = dirname(dirname(abspath(__file__)))
path = join(path, 'datasets/copper.csv')


run = url_to_csv(url = None,
                date_from = '01/01/2022',
                date_to = None,
                asset = 'Copper Futures Historical Data', 
                export_path= path, 
                cur_id= '8831')
run.save_data()
