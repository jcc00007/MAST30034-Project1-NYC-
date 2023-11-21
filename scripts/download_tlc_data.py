from urllib.request import urlretrieve
import urllib.request
import os
import json
import requests
import pandas as pd



####### downloading the tlc data to the landing folder########
output_relative_dir = '../data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ['tlc_data']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/"#year-month.parquet

YEAR = '2018'
# adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc...
# MONTHS = range(1, 13)
MONTHS = range(1, 7)


# data output directory is `data/tlc_data/`
tlc_output_dir = output_relative_dir + 'tlc_data'


for month in MONTHS:
    month = str(month).zfill(2) 
    print(f"Begin month {month}")
    
    yellow = "yellow_tripdata_"
    # generate url
    
    yellow_url = f'{URL_TEMPLATE}{yellow}{YEAR}-{month}.parquet'

    # generate output location and filename
    yellow_output_dir = f"{tlc_output_dir}/{yellow}{YEAR}-{month}.parquet"
    
    # download
    urlretrieve(yellow_url, yellow_output_dir) 
    
    print(f"Completed month {month}")




