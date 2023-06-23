# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 07:58:19 2023

@author: Guey Ling
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd

# Read data from CSV
data = pd.read_csv('Reviews.csv')
sorted_scores = sorted(data['Score'].unique())

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Distribution of the Ratings"),
    dcc.Graph(
        id='histogram-chart',
        figure=px.histogram(data_frame=data, x='Score', nbins=10,
                            labels={'value': 'Score', 'count': 'Frequency', 'color': 'Score'},
                            color='Score',
            color_discrete_sequence=px.colors.qualitative.Plotly,
            category_orders={'Score': sorted_scores}).update_layout(
            bargap=0.2,
            xaxis=dict(
                tickvals=list(range(int(data['Score'].min()), int(data['Score'].max()) + 1)),  # Increase values by 1
                ticktext=list(range(int(data['Score'].min()), int(data['Score'].max()) + 1))  # Set tick text
            ),
            yaxis=dict(
                title='Count'  # Set the custom y-axis name
            )
        ).update_traces(
            marker=dict(line=dict(color='#000000', width=2))
        )
    )
])
            
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)