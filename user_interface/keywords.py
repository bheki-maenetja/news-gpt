# Third-Party Imports
from dash import html, dcc

def get_keywords():
    return html.Div(
        id="word-cloud-section",
        className="word-cloud-section",
        children=[
            html.Div(
                id="word-cloud-params",
                className="word-cloud-params",
                children=[
                    html.Button(
                        id="word-cloud-btn",
                        className="word-cloud-btn",
                        children="Generate Word Cloud",
                    ),
                ]
            ),
            html.Div(
                id="word-cloud-output",
                className="word-cloud-output",
                children=[
                    dcc.Loading(
                        color="#003049",
                        children=[
                            html.Div(
                                id="word-cloud-plot",
                                className="word-cloud-plot",
                            )
                        ]
                    )
                ]
            )
        ]
    )