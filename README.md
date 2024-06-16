## AirBnB Data Analysis and Visualization
### Problem Statement:
#### This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. 
#### Following are the steps followed as part of this Project
#### 1. Data Cleaning & preparation
#### 2. Geospatial Visualization 
#### 3. Price Analysis and Visualization
#### 4. Property Availabilty over different years & different months in a year 
#### 5. Location-Based Insights 

###### Link for dataset : https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view
###### Download & store in the Data folder within the project

#### Setting up the python Environment 
```conda create -p airbnbenv python==3.10```

#### Install all the requirements 
```pip install -r requirements.txt```

#### Data Extraction from json
``` python data_extraction.py```

#### Run the streamlit app 
``` streamlit run app.py```
#### Click on Home Page to get basic details about the Project 
#### Click on "Overall Data Analysis" to view the Visualization related to all the properties across globe
#### Click on "Country Based Analysis" to view the Visualization related to each country/City/Property type. 
#### Following are the graphs provided for visualizing the data
#### 1. Pie Chart - Average Property Price across different countries 
####              - Count of Properties across different countries
#### 2. Line Graph - Occupancy Count over different Years
####               - Occupancy Count over different months in a year 
#### 3. Stacked bar Graph - Total vs Available Properties across different Countries 
#### 4. Geospatial Map Listings - Providing an overview of Properties across globe  
