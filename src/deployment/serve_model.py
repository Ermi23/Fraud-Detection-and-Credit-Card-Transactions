from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('../../models/random_forest_model.pkl')

# Set up logging
logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON request and convert it to DataFrame
        data = request.get_json()
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)

        # Log the request and prediction
        logging.info(f"Request data: {data}, Prediction: {prediction[0]}")

        # Return the prediction result
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.0', port=5000)
