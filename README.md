# Stock Trend Predictor
 Code and report for the development of a machine learning-based stock price direction. All code is written in Python.

## Overview
The project consists in 3 Jupyter Notebooks:
1. Data Exploration
	* Retrieves stock data to use for training the AI models
	* Preprocesses, stores, and gives format to the downloaded data.
	* Selects and calculates features to feed the AI models and creates files for training and testing data for every model to be trained.
2. Model Training
	* Defines the AI model architecture.
	* Connects to Amazon Web Services to instantiate the machine learning models to train with Sagemaker.
	* Trains, deploys, and evaluates the models.
	* Stores the evaluation results locally.
3. Results Analysis
	* Computes the results with visuals.
	* Compares the results to a benchmark model. 

The data and results folders contain already processed data and results. The source folder contains the model definition. 

## Requirements
To run the Jupyter Notebooks correctly you need the following libraries:
1. Pandas-datareader, allows connecting to various stock exchanges and and financial platforms to download stock quotes and convert them into Pandas DataFrames.
2. Yfinance, a package developed by [Ran Aroussi](aroussi.com) that downloads stock quotes from Yahoo Finance and converts them into Pandas DataFrames.
3. Pandas
4. Scikit-learn


Also, some environment variables are needed to train the instances:
1. AWS_ACCESS_KEY: the API access key for your AWS account.
2. AWS_SECREt_KEY: the API secret key for your AWS account.
3. AWS_SAGEMAKER_ROLE: the IAM Role for the model. It must give all Sagemaker permissions.

Important notes:
* The region for the AWS account must be 'us-east-2', unless you change it from the hardcoded Notebook.
* The account should have at least a 20 instance limit for 'ml.p2.2xlarge' and/or 'ml.p2.xlarge'.
