# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 09:36:09 2023

@author: Guey Ling
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# Read data from CSV
data = pd.read_csv('Reviews.csv')

data["Score"] = data["Score"].apply(lambda x: 0 if x < 3 else 1)
labels = ['Recommended', 'Not Recommended']
values = [
    data[data['Score'] == 1]['Score'].value_counts()[1],
    data[data['Score'] == 0]['Score'].value_counts()[0]
]
colors = ['green', 'red']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, opacity=0.8)])
fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2), colors=colors))


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Distribution of the Recommendations"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)