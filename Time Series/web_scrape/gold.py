#Imports
from url_to_csv.scraper import *
from os.path import dirname, abspath, join

path = dirname(dirname(abspath(__file__)))
path = join(path, 'datasets/gold.csv')


run = url_to_csv(url = None,
                date_from = '01/01/2020',
                date_to = None,
                asset = 'Gold Futures Historical Data', 
                export_path= path,
                cur_id= '8830')
run.save_data()
