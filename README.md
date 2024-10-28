# Fraud-Detection-and-Credit-Card-Transactions
This project demonstrates the development and deployment of a fraud detection model using machine learning, Flask, Dash, and Docker. The model is designed to identify fraudulent transactions in credit card and e-commerce data. The project also incorporates explainability techniques (SHAP and LIME) and an interactive dashboard for visual insights.

## Table of Contents
### Introduction
### Project Overview
#### Task 1: Data Preparation and Feature Engineering
#### Task 2: Model Training and Evaluation
#### Task 3: Model Explainability
#### Task 4: Model Deployment and API Development
#### Task 5: Dashboard Development with Flask and Dash
### Datasets
### Setup Instructions
### API Usage
### Conclusion


### Introduction

This project involves building a fraud detection model from scratch, explaining its predictions using SHAP and LIME, deploying it as a REST API, and creating a dashboard with Dash to visualize insights about fraud patterns.

### Project Overview
#### Task 1: Data Preparation and Feature Engineering
1. Data Loading: Load datasets into pandas DataFrames for analysis and preprocessing.

2. Handling Missing Values: Impute or drop missing values to maintain data integrity.

3. Data Cleaning: Remove duplicate entries, correct data types, and preprocess data for consistency.

4. Exploratory Data Analysis (EDA): Perform univariate and bivariate analysis to understand feature distributions and relationships.

5. Geolocation Analysis: Merge datasets to map IP addresses to countries.

6. Feature Engineering: Create new features such as time differences, hour and day of transactions, and geolocation mappings.

7. Normalization and Scaling: Scale numerical features and encode categorical features.

8. Data Splitting: Split data into training and test sets for model training.

#### Task 2: Model Training and Evaluation

1. Model Selection: Select machine learning algorithms for fraud detection, including Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, and MLP.

2. Training: Train selected models on the processed credit card data.

3. Evaluation: Assess model performance using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.

#### Task 3: Model Explainability
1. SHAP and LIME Integration: Use SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) to interpret the model’s predictions.

2. Visualizations: Generate SHAP summary plots, force plots, and dependence plots to analyze feature importance and relationships.

#### Task 4: Model Deployment and API Development
1. Flask API Setup: Create a Flask API to serve the trained model for prediction requests.
2. API Development: Define /predict endpoint for making predictions.
3. Dockerization: Containerize the Flask application using Docker for easy deployment.

#### Task 5: Dashboard Development with Flask and Dash
1. Flask Backend: Serve data through Flask endpoints that summarize fraud trends.

2. Dash Frontend: Create interactive visualizations of fraud insights using Dash.

* Summary boxes to display total transactions, fraud cases, and fraud percentages.
* Line chart for fraud trends over time.
* Bar charts for fraud cases across devices and browsers.
* Map visualization for fraud cases by geographic location.

#### Datasets
* Fraud_Data.csv
This dataset includes e-commerce transaction data for fraud detection. Key features:

user_id: Unique identifier for the user.
signup_time: User signup timestamp.
purchase_time: Transaction timestamp.
purchase_value: Transaction value.
device_id: Device identifier.
source: Source of the user (e.g., Ads, SEO).
browser: Browser used.
sex: Gender of the user.
age: Age of the user.
ip_address: Transaction IP address.
class: Target indicating fraudulent (1) or non-fraudulent (0).

* IpAddress_to_Country.csv
Maps IP ranges to countries for geolocation insights.

* creditcard.csv
Bank transaction dataset for fraud detection with features such as:

Time: Time elapsed since the first transaction.
V1 to V28: Anonymized features.
Amount: Transaction value.
Class: Target variable (1 for fraud, 0 for non-fraud).

#### Setup Instructions
Prerequisites
Python 3.8+
Docker

#### Installation
* Clone the repository:

git clone https://github.com/Ermi23/Fraud-Detection-and-Credit-Card-Transactions.git
cd Fraud-Detection-and-Credit-Card-Transactions

* Create a virtual environment and activate it:

python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate

* Install the dependencies:

pip install -r requirements.txt

* Run the Flask application for the API:

python src/dashboard/app.py

* Run the Dash dashboard:

python src/dashboard/dash_app.py

#### Docker Setup
* Build the Docker image:

docker build -t fraud-detection-model .

* Run the Docker container:

docker run -p 5000:5000 fraud-detection-model

#### API Usage

* Endpoint: /predict
Method: POST
Content-Type: application/json
Request Body: JSON object with relevant transaction features (e.g., purchase_value, age, source, browser, etc.).

Example Request:
json

{
  "purchase_value": 150,
  "age": 34,
  "source": "SEO",
  "browser": "Chrome",
  "sex": "M",
  "signup_hour": 14,
  "signup_day": 3,
  "purchase_hour": 16,
  "purchase_day": 5
}
Example Response:
json

{
  "prediction": 1
}

#### Conclusion
This project covers the complete lifecycle of building a fraud detection system:

1. Data Preparation with cleaning, feature engineering, and geolocation analysis.
2. Model Building and Evaluation to select the best-performing algorithms.
3. Explainability using SHAP and LIME to understand model predictions.
4. Deployment as a REST API and visualization with an interactive Dashboard.

The project demonstrates not only the creation of a robust fraud detection model but also the use of Flask, Dash, Docker, and explainability techniques to make it functional, interpretable, and ready for deployment.