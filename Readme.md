Titanic Dataset Analysis
Overview
This project involves the analysis of the Titanic dataset using various Python scripts. The dataset contains information about passengers aboard the Titanic, including details such as passenger ID, survival status, class, name, sex, age, ticket information, fare, cabin, and embarked port.

Contents
Scripts:

load.py: Python script to load and preprocess the Titanic dataset.
dpre.py: Python script for data preprocessing.
eda.py: Python script for exploratory data analysis.
vis.py: Python script for data visualization.
model.py: Python script for machine learning modeling and clustering.
final.ps1: PowerShell script to copy output files from the Docker container to the local system and stop the container,and we use final.ps1 not final.sh because we use windows not linux
Data:

train_titanic.csv: The Titanic dataset used for analysis.
Logs:

logs.txt: Contains the logs of script executions and any errors encountered during the process.
Usage
Load and Preprocess Data:

Run load.py to load the dataset and preprocess it. Example command:
lua
Copy code
python3 load.py train_titanic.csv
Exploratory Data Analysis (EDA):

After loading and preprocessing the data, run eda.py for exploratory data analysis.
Data Visualization:

Execute vis.py to generate visualizations based on the preprocessed data.
Machine Learning Modeling and Clustering:

Run model.py for machine learning modeling and clustering on the preprocessed dataset.
Copying Output Files and Stopping Docker Container (Windows):

Use final.ps1 to copy output files from the Docker container to the local system and stop the container.
Logs
The logs.txt file contains detailed logs of each script execution, including any errors encountered during the process.

Requirements
Python 3.x
Pandas
Matplotlib
Scikit-learn
Docker (for running the analysis in a containerized environment)
Contributors
Ali Hamed
Ammar Nashaat
Hussein Osama