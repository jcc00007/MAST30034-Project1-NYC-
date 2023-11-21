import os
import requests
import pandas as pd

####### downloading the tlc data to the landing folder########
output_relative_dir = '../data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
# now, for each type of data set we will need, we will create the paths
for target_dir in ['weather_data']: # taxi_zones should already exist
    if not os.path.exists(output_relative_dir + target_dir):
        os.makedirs(output_relative_dir + target_dir)


# data output directory is `data/weather_data/`
output_dir = output_relative_dir + 'weather_data'


### it is really hard to souce hourly data, i found this free website, but there is limit to amount of data per account
### , so i made a numer of account and access each individual month's data 


##### january 
# URL of the Excel file
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=3KV39RDEE5QHS9NHX8BR86DZV&taskId=2af03f463bbd5f9cce772cd0c94d441c&zip=false"

# Send a GET request to download the file
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_jan.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)

#### Febuary 
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=MSD8D4D4A282PQKXAUZSKQF6F&taskId=611a286309a2873e982d50e2d70c661a&zip=false"
# Send a GET request to download the file
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_feb.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)


#### March
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=3KV39RDEE5QHS9NHX8BR86DZV&taskId=b0b0af04b27747fa6248069ceb962785&zip=false'
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_march-1.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)


url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=MSD8D4D4A282PQKXAUZSKQF6F&taskId=4a29c1d445470f041e9eed645cc04d92&zip=false'
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_march-2.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)



##### april 

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=NPB96UWQBZWW7N92HH5A2KJMF&taskId=3f0de2c43aa9f7c8da8ca91ce51f1210&zip=false'
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_april.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)




###### may 
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=KSU9WMZYY5L38DPS633ZH8MU6&taskId=66836c96b65c72ce98f72d8e6c8eae6d&zip=false"
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_may.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)



######## june

url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=AVWLMLSSQLWTASXA3UFXLANK3&taskId=39d542119fefd5c01c0353be4c74cae7&zip=false'
response = requests.get(url)

# Specify the local file path to save the downloaded Excel file
local_file_path = output_dir+"/weather_data_jun.csv"

# Write the content of the response to the local file
with open(local_file_path, "wb") as file:
    file.write(response.content)
