[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LOuMvgtV)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11503429&assignment_repo_type=AssignmentRepo)
# MAST30034 Project 1 README.md
- Name: `Jincong Chen`
- Student ID: `1264476`

**Research Goal:** My research goal to classifying pick-up hotspots, identifying high-demand periods (hourly) and investigating factors that influence driver tips.

**Timeline:** The timeline for the research area is 2018 Jan to June.

To run the pipeline, please visit the `notebook` directory and run the files in order:
1. `1_Download_data.ipynb`: This downloads the all raw data inlcuding external data and testing data into the `data/landing` directory.
2. `2_Preprocessing-taxi-data.ipynb`: This notebook performs preprocessing steps with tlc data and outputs it to the `data/raw` and `data/curated` directory.
3. `3_Preprocess_taxi_zone.ipynb`: This notebook performs preprocessing and aggregating the taxi zone/ took up table asn save as geospandas data frame in `data/curated`.
4. `4_Preprocess-gasoline-data.ipynb`:  This notebook performs preprocessing to gasoline data and save to `data/curated`.
5. `5_Preprocess_weather_data.ipynb` : This notebook performs data preprocessing to weather data and save the ouput to the `data/raw` and `data/curated` directory.
6. `6_Preprocess_and_merge_test_data.ipynb`: This notebook performs data preprocessing to our test data such as weather data and tlc taxi data in march 2019 and save the output to the `data/raw` and `data/curated` directory.
7. `Analysis-part1.ipynb`: This notebook used to conduct analysis on the curated data. Examine the distribution of key feature in tlc data, and perform aggregation with gasoline data to analysis in relationship between gaosline price and taxi demand. There will be a number of plot made and output to `plots` directory #### This section also have some weekly analysis that i didn;t inlcude in the report due to the limted page number.
8. `Analysis-part2_weather.ipynb` :  This notebook used to conduct analysis on the curated data. Examine relationship between weather condition with taxi demand. series of plot will be output to the`plots` directory
10. `Geographic_analysis .ipynb`: This notebook used to conduct analysis on the curated data. Performinggeospatial analysis, aggregating taxi and taxi zone data. Plots will be ouput to the`plots` directory. ########### There is also extra analysis on proportion of fare amount in each location which i didn't include in the report due to the page limit
12.   `Modeling.ipynb`: This notebook is used to perform, analysing and discussing the model. Predicitng the average hourly taxi demand at manhattan during time period of March 2019. 
