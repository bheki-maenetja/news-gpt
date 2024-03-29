# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_editorial():
    return html.Div(
        id="editorial-section",
        className="editorial-section",
        children=[
            html.Div(
                id="editorial-params",
                className="editorial-params",
                children=[
                    dcc.Slider(
                        id="editorial-slider",
                        className="editorial-slider",
                        min=-3,
                        max=3,
                        step=1,
                        value=0,
                        included=False,
                        marks={
                            -3: "Far Left",
                            -2: "Progressive",
                            -1: "Liberal",
                            0: "Centrist",
                            1: "Conservative",
                            2: "Right Wing",
                            3: "AltRight",
                        },
                    ),
                    html.Button(
                        id="editorial-btn",
                        className="editorial-btn",
                        children="Create Editorial",
                    ),
                    html.Button(
                        id="editorial-download-btn",
                        className="editorial-btn disabled",
                        disabled=True,
                        children="Download",
                    ),
                    dcc.Download(id="download-editorial"),
                    html.Button(
                        id="editorial-clear-btn",
                        className="editorial-btn disabled",
                        disabled=True,
                        children="Clear",
                    ),
                ]
            ),
            html.Div(
                id="editorial-output",
                className="editorial-output",
                children=[
                    html.Div(
                        id="editorial-output-content-container",
                        className="editorial-output-content-container",
                        children=[
                            dcc.Loading(
                                color="#780000",
                                children=[
                                    dbc.Textarea(
                                        id="editorial-output-content",
                                        className="editorial-output-content",
                                        value="",
                                        draggable=False,
                                        readOnly=True,
                                        placeholder="Create an editorial for today's headlines"
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            ),
        ]
    )