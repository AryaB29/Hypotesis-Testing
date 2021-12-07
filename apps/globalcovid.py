from dash.dcc.Graph import Graph
import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app #change this line

# Data Preprocessing
data1 = pd.read_csv('Data Female Cash.csv')
data2 = pd.read_csv('Data Male Cash.csv')
data3 = pd.read_csv('data_cash.csv')
data4 = pd.read_csv('data_E_Wallet.csv')
data5 = pd.read_csv('Data Female Ewallet.csv')
data6 = pd.read_csv('Data Male Ewallet.csv')

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Data Penjualan Supermarket"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualisasi mengenai data penjualan Data'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_type',
                    options=[
                       {'label':'Data Keseluruhan Cash', 'value' : 'Data Keseluruhan Cash'},
                       {'label':'Data Keseluruhan Ewallet', 'value' : 'Data Keseluruhan Ewallet'},
                       {'label':'Data Pembelanjaan Cash Laki Laki', 'value' : 'Data Pembelanjaan Cash Laki Laki'},
                       {'label':'Data Pembelanjaan Cash Perempuan', 'value' : 'Data Pembelanjaan Cash Perempuan'},
                       {'label':'Data Pembelanjaan Ewallet Laki Laki', 'value' : 'Data Pembelanjaan Ewallet Laki Laki'},
                       {'label':'Data Pembelanjaan Ewallet Perempuan', 'value' : 'Data Pembelanjaan Ewallet Perempuan'},
                    ],
                    value='Data Keseluruhan Cash',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                )
            )
        ]),
    ])
])

@app.callback(
    Output('main-graph', 'figure'),
    Input('selected_type', 'value')
)
def update_covid_chart(value):
    if value == 'Data Pembelanjaan Cash Laki Laki':
        databar_male_cash = data2['Product line'].value_counts().index
        databar_male_cash2 = data2['Product line'].value_counts().values
        fig = px.bar(data2, x= databar_male_cash, y= databar_male_cash2, title="Jumlah Pembelian Berdasarkan Tipe Barang Untuk laki laki Menggunakan Cash")
    if value == 'Data Pembelanjaan Cash Perempuan':
        databar_female_cash = data1['Product line'].value_counts().index
        databar_female_cash2 = data1['Product line'].value_counts().values
        fig = px.bar(data1, x= databar_female_cash, y= databar_female_cash2, title="Jumlah Pembelian Berdasarkan Tipe Barang Untuk Perempuan Menggunakan Cash")
    if value == 'Data Keseluruhan Cash':
        jumlah_gender = data3['Gender'].value_counts().values
        jenis_gender = data3['Gender'].value_counts().index
        fig = px.pie(data3, values= jumlah_gender , names= jenis_gender,title='Presentase Jumlah Pemakai Cash Berdasar Gender')
    if value == 'Data Keseluruhan Ewallet':
        jumlah_gender = data4['Gender'].value_counts().values
        jenis_gender = data4['Gender'].value_counts().index
        fig = px.pie(data4, values= jumlah_gender , names= jenis_gender,title='Presentase Jumlah Pemakai Ewallet Berdasar Gender')
    if value == 'Data Pembelanjaan Ewallet Laki Laki':
        databar_male_ewallet = data6['Product line'].value_counts().index
        databar_male_ewallet2 = data6['Product line'].value_counts().values
        fig = px.bar(data6, x= databar_male_ewallet, y= databar_male_ewallet2, title="Jumlah Pembelian Berdasarkan Tipe Barang Untuk Laki Laki Menggunakan Ewallet")
    if value == 'Data Pembelanjaan Ewallet Perempuan':
        databar_female_ewallet = data5['Product line'].value_counts().index
        databar_female_ewallet2 = data5['Product line'].value_counts().values
        fig =px.bar(data5, x= databar_female_ewallet, y= databar_female_ewallet2, title="Jumlah Pembelian Berdasarkan Tipe Barang Untuk Perempuan Menggunakan Ewallet")
    return fig


# remove the main things