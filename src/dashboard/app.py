from flask import Flask, jsonify
import pandas as pd

import os
print(os.getcwd())  # This prints the current working directory

# Initialize the Flask app
app = Flask(__name__)

# Load the fraud data (replace with path to actual fraud data)
fraud_data = pd.read_csv('Data/Raw/Fraud_Data.csv')

# Endpoint to get summary statistics
@app.route('/summary', methods=['GET'])
def get_summary():
    total_transactions = len(fraud_data)
    total_fraud_cases = fraud_data[fraud_data['class'] == 1].shape[0]
    fraud_percentage = (total_fraud_cases / total_transactions) * 100

    summary = {
        'total_transactions': total_transactions,
        'total_fraud_cases': total_fraud_cases,
        'fraud_percentage': round(fraud_percentage, 2)
    }
    return jsonify(summary)

# Endpoint to get fraud trends over time
@app.route('/fraud_trends', methods=['GET'])
def get_fraud_trends():
    fraud_trends = fraud_data[fraud_data['class'] == 1].groupby('date').size().reset_index(name='fraud_cases')
    return fraud_trends.to_json(orient='records')

if __name__ == '__main__':
    app.run(port=5001)
