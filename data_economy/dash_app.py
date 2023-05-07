from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
import dash

app = DjangoDash('SimpleExample')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])


@app.callback(
    dash.dependencies.Output('graph-content', 'figure'),
    [dash.dependencies.Input('dropdown-selection', 'value')])
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')



# from dash import Dash, html, dcc, callback, Output, Input
# import plotly.express as px
# from django_plotly_dash import DjangoDash
# import dash
#
# class DashPlotly:
#     def __init__(self, df):
#         self.app = DjangoDash('SimpleExample')
#         self.df = df
#         self.app.layout = html.Div([
#             html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
#             dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
#             dcc.Graph(id='graph-content')
#         ])
#
#         @self.app.callback(
#             dash.dependencies.Output('graph-content', 'figure'),
#             [dash.dependencies.Input('dropdown-selection', 'value')])
#         def update_graph(value):
#             dff = self.df[self.df.country == value]
#             return px.line(dff, x='year', y='pop')
