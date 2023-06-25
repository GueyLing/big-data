# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 09:52:00 2023

@author: Guey Ling
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv('Reviews.csv')

data_recommended = data[data['Score'] == 1]

wordcloud = WordCloud(max_words=500, random_state=500, collocations=True).generate(str((data_recommended['Text'])))

# Convert WordCloud object to plotly object
wordcloud_plotly = go.Figure(data=[go.Image(z=wordcloud.to_array())])

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Frequent Words in Recommended Reviews"),
        dcc.Graph(figure=wordcloud_plotly)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)