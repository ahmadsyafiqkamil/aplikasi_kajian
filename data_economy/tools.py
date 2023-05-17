import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from statsmodels.tsa.api import ExponentialSmoothing
# from statsmodels.tsa.holtwinters import ExponentialSmoothing


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


def plot_coloumn(df):
    fig = go.Figure()

    # menambahkan data ke dalam plot
    fig.add_trace(go.Scatter(x=df['tahun'], y=df['Data'], mode='lines'))

    # menentukan layout plot
    fig.update_layout(title='Seluruh Data', xaxis_title='Tahun', yaxis_title='Data')

    tahun = df['tahun'].unique()
    bulan = df['bulan'].unique()
    vervar = df['vervar'].unique()
    karakteristik = df['karakteristik'].unique()

    button_layer_1_height = 1.08
    fig.update_layout(
        updatemenus=[
            go.layout.Updatemenu(
                buttons=[
                    {
                        'label': f"{t}",
                        'method': 'update',
                        'args': [
                            {'x': [df.loc[(df['tahun'] == t)]['tahun']],
                             'y': [df.loc[(df['tahun'] == t)]['data']],
                             'name': f'Data {t}'
                             },
                            {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                        ]
                    } for t in tahun
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0,
                xanchor="left",
                y=button_layer_1_height,
                yanchor="top",
                active=0
            ),
            go.layout.Updatemenu(
                buttons=[
                    {
                        'label': f"{b}",
                        'method': 'update',
                        'args': [
                            {'x': [df.loc[(df['bulan'] == b)]['tahun']],
                             'y': [df.loc[(df['bulan'] == b)]['data']],
                             'name': f'Data {b}'
                             },
                            {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                        ]
                    } for b in bulan
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=button_layer_1_height,
                yanchor="top",
                active=0,

            ),
            go.layout.Updatemenu(
                buttons=[
                    {
                        'label': f"{v}",
                        'method': 'update',
                        'args': [
                            {'x': [df.loc[(df['vervar'] == v)]['tahun']],
                             'y': [df.loc[(df['vervar'] == v)]['data']],
                             'name': f'Data {v}'
                             },
                            {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                        ]
                    } for v in vervar
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.6,
                xanchor="left",
                y=button_layer_1_height,
                yanchor="top",
                active=0,
            ),
            go.layout.Updatemenu(
                buttons=[
                    {
                        'label': f"{b}",
                        'method': 'update',
                        'args': [
                            {'x': [df.loc[(df['karakteristik'] == b)]['tahun']],
                             'y': [df.loc[(df['karakteristik'] == b)]['data']],
                             'name': f'Data {b}'
                             },
                            {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                        ]
                    } for b in karakteristik
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.8,
                xanchor="left",
                y=button_layer_1_height,
                yanchor="top",
                active=0,
            ),
            go.layout.Updatemenu(
                buttons=
                [
                    {
                        'label': 'Seluruh Data',
                        'method': 'update',
                        'args': [
                            {'x': [df['tahun']],
                             'y': [df['data']],
                             'name': 'Seluruh Data'
                             },
                            {'xaxis.title': 'Tahun', 'yaxis.title': 'Data'}
                        ]
                    }
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.4,
                xanchor="left",
                y=button_layer_1_height,
                yanchor="top",
                active=0
            ),
        ]
    )

    fig_json = pio.to_json(fig)
    # plot_html = opy.plot(fig, auto_open=False, output_type='div')
    # context = {'plot': plot_html}
    return fig_json


def predict(df):


    # data_baru = df.loc[:,["tahun","Data"]]
    # data_baru.set_index('tahun')
    # print(df)
    df.set_index('tahun')


    model = ExponentialSmoothing(df['Data'],  seasonal='add', seasonal_periods=2)

    # Melakukan prediksi untuk 5 tahun ke depan
    forecast = model.fit().forecast(steps=5)

    # Mengonversi nilai tahun ke tipe data integer
    last_year = int(df['tahun'].max())
    tahun_prediksi = pd.RangeIndex(start=last_year + 1, stop=last_year + 6)
    df_pred = pd.DataFrame({'tahun': tahun_prediksi, 'Prediksi': forecast.values})

    # Menggabungkan data asli, prediksi, dan data sebelumnya
    df_hasil = pd.concat([df, df_pred], axis=0)
    df_reset = df_hasil.reset_index()
    df_reset = df_reset.drop("index", axis=1)
    # Menampilkan hasil prediksi dan plot
    # print(forecast)
    # print(df_reset)
    return df_reset


def plot_predict(df):
    # print(df)
    fig = go.Figure()

    fig.update_layout(title='Hasil Prediksi', xaxis_title='Tahun', yaxis_title='Data')

    # Menambahkan data prediksi
    fig.add_trace(go.Scatter(x=df['tahun'], y=df['Prediksi'], mode='lines', name='Prediksi'))

    # Menambahkan data asli
    fig.add_trace(go.Scatter(x=df['tahun'], y=df['Data'], mode='lines', name='Data'))

    fig_json = pio.to_json(fig)
    return fig_json
