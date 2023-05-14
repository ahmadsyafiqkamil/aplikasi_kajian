import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from django.conf import settings
import plotly.graph_objects as go
import plotly.offline as opy
import plotly.io as pio
from plotly.offline import init_notebook_mode, iplot


def json_to_pd(data_dict):
    data_tuples = []
    # Iterate through each key in data_dict and convert to tuple
    for key, value in data_dict['data'].items():
        # Remove brackets and quotes from key string, and split on comma
        key_parts = key.replace('\'', '').replace('(', '').replace(')', '').split(',')
        # Convert each part of key to a tuple
        index = tuple([x.strip() for x in key_parts])
        data_tuples.append(index + (value,))

    # Create pandas DataFrame with multi-index
    df = pd.DataFrame(data_tuples, columns=['tahun', 'bulan', 'vervar', 'karakteristik', 'data_key', 'Data'])
    df = df.set_index(['tahun', 'bulan', 'vervar', 'karakteristik', 'data_key'])
    df_reset = df.reset_index()
    return df_reset


def plot_view(df):
    fig = go.Figure()

    # menambahkan data ke dalam plot
    fig.add_trace(go.Scatter(x=df['tahun'], y=df['Data'], mode='lines'))

    # menentukan layout plot
    fig.update_layout(title='Seluruh Data', xaxis_title='Tahun', yaxis_title='Data')

    # membuat dropdown
    karakteristik = df['karakteristik'].unique()
    vervar = df['vervar'].unique()
    data_values = df['Data'].unique()

    fig.update_layout(
        updatemenus=[
            go.layout.Updatemenu(
                buttons=[
                            {
                                'label': 'Seluruh Data',
                                'method': 'update',
                                'args': [
                                    {'x': [df['tahun']],
                                     'y': [df['Data']],
                                     'name': 'Seluruh Data'
                                     },
                                    {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                                ]
                            }
                        ] + [
                            {
                                'label': f"{k} - {v}",
                                'method': 'update',
                                'args': [
                                    {'x': [df.loc[(df['karakteristik'] == k) & (df['vervar'] == v)]['tahun']],
                                     'y': [df.loc[(df['karakteristik'] == k) & (df['vervar'] == v)]['Data']],
                                     'name': 'Data ' + k + ' ' + v
                                     },
                                    {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                                ]
                            } for k in karakteristik for v in vervar
                        ]
            )
        ]
    )
    fig_json = pio.to_json(fig)
    # plot_html = opy.plot(fig, auto_open=False, output_type='div')
    # context = {'plot': plot_html}
    return fig_json