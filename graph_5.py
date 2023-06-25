# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 10:13:06 2023

@author: Guey Ling
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Read data from CSV
data = pd.read_csv('Reviews.csv')

top_1000_rows = data.head(1000).copy()
FreqOfWords = top_1000_rows['Text'].str.split(expand=True).stack().value_counts()
FreqOfWords_top200 = FreqOfWords[:200]

fig = px.treemap(FreqOfWords_top200, path=[FreqOfWords_top200.index], values=0)
fig.update_traces(textinfo="label+value")

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Top Frequent 200 Words in the Dataset (Before Cleaning)"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)