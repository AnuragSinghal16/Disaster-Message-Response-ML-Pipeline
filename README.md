# Disaster-Message-Response-ML-Pipeline
The aim of this project is to analyse messages received from victims or respondents at the time of a disaster to categorize into groups and priorities help prioritise resources accordingly. This data was collated by Appen

The project had 3 main deliverables:
  1. process.py - this script imports and processes text data to be used as an input to the machine learning pipeline
  2. train_classifier.py - this script will use the cleaned data and input this data to a machine learning pipeline to predict categories
  3. run.py - this script will build a web app where the ML model will be hosted.

## Methodology and Scope
1. The target of the analysis is not to attain maximum accuracy from the model but to have a working pipeline. Accuracy will be subject to running various scans using Grid Search and it's computing can take several hours in a real-world data science use case. As part of this learning, the iterations were kept to a minimum
2. The pipeline uses Random Forest Classifier as a parameter to Multi-output Classifier to estimate target variable - this may not be the best approach if we were to build a live use case with this data


## Files
 1. process.py - this script imports and processes text data to be used as an input to the machine learning pipeline
 2. train_classifier.py - this script will use the cleaned data and input this data to a machine learning pipeline to predict categories
 3. run.py - this script will build a web app where the ML model will be hosted.
 4. Data Preparation.ipynb

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`
