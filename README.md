Forest Fire Exploratory Data Analysis (EDA)
Overview
This project analyzes the UCI Forest Fires Dataset to understand how environmental factors like temperature and humidity influence wildfire spread. The goal is to explore patterns and trends using data visualization.

Dataset
Source: UCI Machine Learning Repository - Forest Fires Dataset
Description: The dataset contains meteorological and fire-related data recorded in Portugal's Montesinho park.
Key Features:
Temperature, Relative Humidity, Wind speed, Rain
Burned Area
Categorical variables for Month and Day
Objectives
Analyze historical wildfire occurrences
Investigate the impact of weather conditions on fire spread
Create visualizations to better understand wildfire behavior
Data Processing
Removed missing and corrupted values
Converted categorical variables into numerical format
Standardized weather-related features
Visualizations
Scatter Plot: Temperature vs Burned Area
Shows the relationship between temperature and fire size
Uses a regression line to observe trends
Box Plot: Humidity vs Burned Area
Groups humidity levels into bins
Examines fire size distributions under different humidity conditions
How to Run
Install required libraries:
pip install pandas seaborn matplotlib numpy
Run the script:
python fire_visualization.py
Output images will be saved as:
scatter_plot.png
box_plot.png