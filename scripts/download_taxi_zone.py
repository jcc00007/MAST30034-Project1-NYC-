from urllib.request import urlretrieve
import urllib.request
import os
import requests
import pandas as pd


####### downloading the taxi_zone lookup csv to the landing folder########
output_relative_dir = '../data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ['taxi_zone']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)

taxi_zone_lookup_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"


# data output directory is `data/tlc_data/`
taxi_zone_output_dir = output_relative_dir + 'taxi_zone'


# Get the content of the CSV file from the URL
response = requests.get(taxi_zone_lookup_url)
if response.status_code == 200:
    # Save the content to a local CSV file
    csv_file_path = os.path.join(taxi_zone_output_dir, "taxi_zone.csv")
    with open(csv_file_path, 'wb') as f:
        f.write(response.content)


############## download Taxi Zone Shapefile to the same folder 
taxi_zone_shapefile_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip"

response = requests.get(taxi_zone_shapefile_url)
if response.status_code == 200:
    # Save the content to a local ZIP file
    zip_file_path = os.path.join(taxi_zone_output_dir, "taxi_zone_file.zip")
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)



