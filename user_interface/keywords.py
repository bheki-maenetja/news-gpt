# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

def get_keywords():
    return html.Div(
        id="word-cloud-section",
        className="word-cloud-section",
        children=[
            html.Div(
                id="word-cloud-params",
                className="word-cloud-params",
                children=[
                    html.Button("Generate Word Cloud"),
                ]
            ),
            html.Div(
                id="word-cloud-output",
                className="word-cloud-output",
                children=[
                    dcc.Loading([
                        dcc.Graph(
                            id="word-cloud-plot",
                            figure=go.Figure(),
                        )
                    ])
                ]
            )
        ]
    )