import os
import requests
import pandas as pd


####### downloading the tlc data to the landing folder########
output_relative_dir = '../data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ['gasoline_data']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)


# data output directory is `data/gasoline_data/`
output_dir = output_relative_dir + 'gasoline_data'

# URL of the Excel file
url = "https://www.eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls"

# Send a GET request to download the file
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/gasoline_data.xls"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)

