# Fraud-Detection-and-Credit-Card-Transactions

This project demonstrates the development and deployment of a fraud detection model using machine learning, Flask, and Docker.

## Table of Contents

- [Introduction](#introduction)
- [Tasks Overview](#tasks-overview)
  - [Task 1: Data Preprocessing and Feature Engineering](#task-1-data-preprocessing-and-feature-engineering)
  - [Task 2: Model Training and Evaluation](#task-2-model-training-and-evaluation)
  - [Task 3: Model Explanation with SHAP](#task-3-model-explanation-with-shap)
  - [Task 4: Model Deployment and API Development](#task-4-model-deployment-and-api-development)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)

## Introduction

This project involves building a fraud detection model, explaining its predictions with SHAP, and deploying it as a REST API using Flask and Docker.

## Tasks Overview

### Task 1: Data Preprocessing and Feature Engineering

1. **Data Cleaning**: Handle missing values, outliers, and irrelevant features.
2. **Feature Engineering**: Create new features from existing data to improve model performance.
3. **Data Splitting**: Split the data into training and testing sets.

### Task 2: Model Training and Evaluation

1. **Model Selection**: Choose appropriate machine learning algorithms.
2. **Training**: Train the model using the training data.
3. **Evaluation**: Evaluate the model's performance using the test data.

### Task 3: Model Explanation with SHAP

1. **SHAP Integration**: Use SHAP to explain the model's predictions.
2. **Visualizations**: Generate SHAP summary plots and dependence plots to interpret the model.

### Task 4: Model Deployment and API Development

1. **Flask API Setup**: Create a Flask application to serve the model.
2. **API Development**: Define API endpoints for making predictions.
3. **Dockerization**: Containerize the Flask application using Docker.

## Datasets

### Fraud_Data.csv
This dataset includes e-commerce transaction data aimed at identifying fraudulent activities. Key features include:
- `user_id`: Unique identifier for the user.
- `signup_time`: Timestamp when the user signed up.
- `purchase_time`: Timestamp when the purchase was made.
- `purchase_value`: Value of the purchase in dollars.
- `device_id`: Unique identifier for the device used.
- `source`: Source through which the user came to the site.
- `browser`: Browser used for the transaction.
- `sex`: Gender of the user.
- `age`: Age of the user.
- `ip_address`: IP address from which the transaction was made.
- `class`: Target variable indicating fraudulent (1) or non-fraudulent (0) transactions.

### IpAddress_to_Country.csv
This dataset maps IP addresses to countries, with fields including:
- `lower_bound_ip_address`: Lower bound of the IP address range.
- `upper_bound_ip_address`: Upper bound of the IP address range.
- `country`: Country corresponding to the IP address range.

### creditcard.csv
This dataset contains bank transaction data curated for fraud detection analysis, with features such as:
- `Time`: Seconds elapsed between this transaction and the first transaction in the dataset.
- `V1` to `V28`: Anonymized features from a PCA transformation.
- `Amount`: Transaction amount in dollars.
- `Class`: Target variable indicating fraudulent (1) or non-fraudulent (0) transactions.

##  Data Preprocessing and Feature Engineering

### 1. Data Loading
    -Load the datasets into pandas DataFrames for analysis and preprocessing.

### 2. Handle Missing Values
    -Address missing values by either imputing or dropping them to maintain data integrity.

### 3. Data Cleaning
    -Remove duplicate entries and correct data types to ensure consistency and accuracy.

### 4. Exploratory Data Analysis (EDA)
    -Perform univariate and bivariate analysis to understand the distribution and relationships of the features. This includes visualizing the distribution of the target variable and other key features.

### 5. Geolocation Analysis
    -Convert IP addresses to integer format and merge the datasets to map IP addresses to their respective countries.

### 6. Feature Engineering
    -Create new features to capture additional information from the existing data. Examples include calculating the time difference between signup and purchase, and extracting the hour of the day and day of the week from the purchase time.

### 7. Normalization and Scaling
    -Normalize and scale numerical features to prepare the data for machine learning models.

### 8. Encode Categorical Features
    -Encode categorical features using techniques such as one-hot encoding to convert them into a numerical format suitable for machine learning algorithms.

### 9. Data Splitting:
    -Split the dataset into training and testing sets to evaluate model performance on unseen data.
    -70/30 split is used.

##  Model Training and Evaluation

### 1. Model Selection
    -Choose machine learning algorithms that are suitable for the problem. Common choices for classification tasks include.
        -Logistic Regression
        -Decision Trees
        -Random Forests
        -Gradient Boosting Machines
        -MLP

### 2. Training:
    -Train the selected models using the training data.

### 3. Evaluation
    -Evaluate the model's performance on the test set using metrics such as
        -Accuracy
        -Precision
        -Recall
        -F1 Score
        -ROC-AUC

##  Model Explanation with SHAP and LIME

### 1. SHAP Integration
    -Use SHAP (SHapley Additive exPlanations) and LIME(Local Interpretable Model-agnostic Explanations) to explain the model's predictions.
    -SHAP LIME values provide insights into the contribution of each feature to the prediction.

### 2. Visualizations:
    -Generate SHAP and LIME summary plots to visualize feature importance.
    -Create SHAP LIME dependence plots to understand the relationship between features and the target variable.

##  Model Deployment and API Development

### 1. Flask API Setup
    -Create a Flask application to serve the trained model as an API.
    -Load the trained model and define endpoints for making predictions.

### 2. API Development:
    -Define API endpoints using Flask's routing mechanism

### 3. Dockerization:
    -Create a Dockerfile to containerize the Flask application.
    -Docker allows for easy deployment and scalability of the application.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Docker

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Ermi23/Fraud-Detection-and-Credit-Card-Transactions.git
    cd fraud_detection_model
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```sh
    python serve_model.py
    ```

### Docker Setup

1. **Build the Docker image**:

    ```sh
    docker build -t fraud-detection-model .
    ```

2. **Run the Docker container**:

    ```sh
    docker run -p 5000:5000 fraud-detection-model
    ```
## API Usage

### Endpoint: `/predict`

- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**: JSON object with the following fields:
  - `purchase_value`: Numeric
  - `age`: Numeric
  - `source`: String (e.g., "Ads", "Direct", "SEO")
  - `browser`: String (e.g., "Chrome", "FireFox", "IE", "Opera", "Safari")
  - `sex`: String (e.g., "M", "F")
  - `signup_hour`: Numeric
  - `signup_day`: Numeric
  - `purchase_hour`: Numeric
  - `purchase_day`: Numeric

### Explanation

- **Introduction**: Provides a brief overview of the project.
- **Tasks Overview**: Summarizes the key tasks involved in the project.
- **Setup Instructions**: Details the steps for setting up the project environment and running the application.
- **API Usage**:
## Conclusion

This project involves a comprehensive data preprocessing pipeline to prepare the data for model training. The steps include handling missing values, cleaning the data, performing EDA, merging datasets for geolocation analysis, feature engineering, normalization and scaling, and encoding categorical features. The next steps will involve splitting the data into training and testing sets, building and training machine learning models, and further validating and optimizing these models for fraud detection.
