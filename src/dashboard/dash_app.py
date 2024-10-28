import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__, server=True, url_base_pathname='/dashboard/')

# Fetch summary data from Flask API
summary = requests.get('http://localhost:5001/summary').json()

# Fetch fraud trends data from Flask API
fraud_trends = pd.read_json(requests.get('http://localhost:5001/fraud_trends').text)

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

    # Additional charts here
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=5002)
