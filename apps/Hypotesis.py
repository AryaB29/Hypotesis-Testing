import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from scipy import stats 
import numpy as np

data1 = pd.read_csv('Data Male Cash.csv')
data2 = pd.read_csv('Data Female Cash.csv')
np.random.seed(500)
hasildata1 = np.random.normal(data1['gross income'].mean(), data1['gross income'].mean(), 100)
hasildata2 = np.random.normal(data2['gross income'].mean(), data2['gross income'].std(), 100)
# Independent T-Test
t,p = stats.ttest_ind(hasildata1, hasildata2)
confidence_interval = stats.norm.interval(0.95, hasildata1.mean(), hasildata2.std()) #memasukan nilai confidence interval 95%


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to My Hipotesis Testing",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Hi My Name Is Arya, This Is My Hipotesis testing'),
                className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(
                html.H5(children='Disini saya akan melakukan hypotesis testing, dimana dalam hal ini saya melakukan beberapa Hipotesa yaitu sebagai berikut: H0 == Dimana pelanggan Laki Laki Lebih Banyak Menggunakan Cash Dibandingkan dengan pelanggan perempuan Ha == Dimana Pelanggan Laki Laki Tidak Lebih Banyak Menggunakan Cash Dibandingkan Dengan Pelanggan Perempuan Dimana Saya menerapkan Confidence Interval 95% sehingga treshold nya adalah 0.05'),
                className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Maka Ketika Didapatkan Nilainya Maka didapatkan nilai hypotesisnya adalah'),
                className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='nilai statistik t:0.6694008043930517 \n Nilai p value data:0.5040196544552651 \n Nilai Confidence Interval : (-6.831531850439699, 41.348025565975064)'),
                className="mb-3")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Karena nilai p value diatas 0.05 maka dapat disimpulkan bahwa H0 dapat diterima, sehingga dapat dikatakan pelanggan laki laki lebih banyak menggunakan cash dibandingkan dengan perempuan'),
                className="mb-3")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Atau dapat pula disimpulkan bahwa saja untuk meningkatkan daya bisnis dan meningkatkan penjualan perusahaan maka dapat disimpulkan perlu adanya penambahan adss yang ditujukan pada costumer laki laki pada titik/jenis barang tertentu sesuai dengan data yang tertera'),
                className="mb-3")
        ]),
    ])

])