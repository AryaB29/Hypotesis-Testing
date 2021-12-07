import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to Arya's Dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Hi My Name Is Arya, This is My First Dashboard'),
                className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(
                html.H5(children='Terdapat 2 Hal yang Dapat Kamu Akses Disini, Pertama Adalah Data Penjualan dan kedua Adalah Hypotesis Testing'),
                className="mb-5")
        ]),
                dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Kamu Dapat Download Data Set Asli disini',
                        className="text-center"),
                        dbc.Button("Dataset Asli",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='You Can Visit My Github',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/AryaB29",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])

])