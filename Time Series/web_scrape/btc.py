#Imports
from url_to_csv.scraper import *
from os.path import dirname, abspath, join

path = dirname(dirname(abspath(__file__)))
path = join(path, 'datasets/btc.csv')


run = url_to_csv(url = None,
                date_from = None,
                date_to = None,
                asset = 'BTC/USD Bitfinex Historical Data', 
                export_path= path)
run.save_data()
