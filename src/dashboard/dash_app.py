from dash import Dash, dcc, html
import requests
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize Dash app
app = Dash(__name__, server=True, url_base_pathname='/dashboard/')

# Fetch summary data from Flask API
summary = requests.get('http://localhost:5001/summary').json()

# Fetch fraud trends data and handle JSON response
response = requests.get('http://localhost:5001/fraud_trends')
if response.status_code == 200:
    fraud_trends = pd.DataFrame(response.json())
else:
    print("Error fetching fraud trends data:", response.status_code)
    fraud_trends = pd.DataFrame()  # Empty DataFrame as fallback

# Dashboard layout
app.layout = html.Div(children=[
    html.H1(children='Fraud Detection Dashboard'),
    
    # Summary section
    html.Div([
        html.Div(f'Total Transactions: {summary["total_transactions"]}', className="summary-box"),
        html.Div(f'Total Fraud Cases: {summary["total_fraud_cases"]}', className="summary-box"),
        html.Div(f'Fraud Percentage: {summary["fraud_percentage"]}%', className="summary-box"),
    ], className="summary-section"),

    # Fraud Trends Line Chart
    html.Div([
        html.H2("Fraud Cases Over Time"),
        dcc.Graph(
            id='fraud-trends',
            figure=px.line(fraud_trends, x='date', y='fraud_cases', title='Fraud Cases Over Time')
        )
    ]),

    # Additional charts can be added here
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=5002)
