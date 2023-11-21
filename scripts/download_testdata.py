from urllib.request import urlretrieve
import urllib.request
import os
import json
import requests
import pandas as pd



####### downloading the test data of tlc taxi to the landing folder########
output_relative_dir = '../data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ['test_taxi_2019']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/"#year-month.parquet

YEAR = '2019'
MONTHS = range(3,4)

# data output directory is `data/tlc_data/`
tlc_output_dir = output_relative_dir + 'test_taxi_2019'


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



####### downloading the test weather data to the landing folder########

# create new path for the test weather data
for target_dir in ['test_weather_data']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

# api url of the weather data on month march of 2019
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=AVWLMLSSQLWTASXA3UFXLANK3&taskId=827615d7ac85c43343f80abacdbd533d&zip=false"



# Send a GET request to download the file
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = "../data/landing/test_weather_data/test_weather_data.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)

