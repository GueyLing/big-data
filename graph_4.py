# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:17:00 2023

@author: Guey Ling
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('Reviews.csv')

# Convert the 'Time' column to pandas datetime format
df['Time'] = pd.to_datetime(df['Time'], unit='s')

# Set the 'Time' column as the index
df.set_index('Time', inplace=True)

# Resample the data to a desired time frequency, e.g., 'D' for daily, 'M' for monthly
time_distribution = df.resample('D').size()

# Convert the pandas Series to a plotly object
time_distribution_plotly = {
    'data': [{'x': time_distribution.index, 'y': time_distribution.values, 'type': 'line'}],
    'layout': {'xaxis': {'title': 'Time'}, 'yaxis': {'title': 'Frequency'}}
}

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Time Distribution"),
        dcc.Graph(figure=time_distribution_plotly)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)