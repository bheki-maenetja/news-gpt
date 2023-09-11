# Third-Party Imports
from dash import html
import dash_bootstrap_components as dbc

def newsbot_message(message, is_user=True, is_temp=False):
    if is_temp:
        return html.Div(
            id="newsbot-temp-message",
            className="newsbot-message bot",
            children=[
                dbc.Spinner(
                    color="#003049",
                    type="grow",
                    spinner_style={"marginRight": "0.5em"},
                )
                for _ in range(3)
            ]
        )
    return html.Div(
        className=f"newsbot-message {'user' if is_user else 'bot'}",
        children=[
            html.Div(
                className=f"newsbot-message-content {'user' if is_user else 'bot'}",
                children=message,
            )
        ]
    )


def get_newsbot(initial_message):
    return html.Div(
        id="newsbot-section",
        className="newsbot-section",
        children=[
            html.Div(
                id="newsbot-message-space",
                className="newsbot-message-space",
                children=[
                    html.Div([], style={"flexGrow": "1"}),
                    newsbot_message(initial_message, False),
                ]
            ),
            html.Div(
                id="newsbot-params",
                className="newsbot-params",
                children=[
                    dbc.Input(
                        id="newsbot-query",
                        className="newsbot-query",
                        placeholder="Enter your question here",
                        value="",
                        persistence=False,
                    ),
                    html.Button(
                        id="newsbot-btn",
                        className="newsbot-btn disabled",
                        disabled=True,
                        children=[
                            html.I(className="bi bi-send-fill")
                        ]
                    )
                ]
            )
        ]
    )