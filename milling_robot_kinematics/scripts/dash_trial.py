import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H2("Milling Robot Kinematics", style={'text-align': 'center'}),
                html.H5("Kousheek Chakraborty", style={'text-align': 'center'}),
            ], width=True),
        ], align="end"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.H5("Workspace"),
                html.Hr(),
                html.H5("Forward Kinematics"),
                dbc.Col([
                    dbc.Button("-Q1", id="q1_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+Q1", id="q1_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                dbc.Col([
                    dbc.Button("-Q2", id="q2_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+Q2", id="q2_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                dbc.Col([
                    dbc.Button("-D4", id="d4_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+D4", id="d4_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                html.Hr(),
                html.H5("Inverse Kinematics"),
                dbc.Col([
                    dbc.Button("-X", id="x_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+X", id="x_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                dbc.Col([
                    dbc.Button("-Y", id="y_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+Y", id="y_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                dbc.Col([
                    dbc.Button("-Z", id="z_minus", color="primary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                    dbc.Button("+Z", id="z_plus", color="secondary", style={"margin": "5px", "width": "40%"}, n_clicks_timestamp='0'),
                ]),
                html.Hr(),
                html.H5("Trajectory")
            ], width=3),
            dbc.Col([
                dbc.Spinner(
                    dcc.Graph(id='display', style={'height': '80vh'}),
                    color="primary"
                )
            ], width=True)
        ])
    ],
    fluid=True
)

app.run_server(debug=False)