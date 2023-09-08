# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

summary_methods = [
    {"label": "Single Paragraph", "value": "1-para"},
    {"label": "Multiple Paragraphs", "value": "multi-para"},
    {"label": "Short Essay", "value": "s-essay"},
    {"label": "Long Essay", "value": "l-essay"},
    {"label": "Short List", "value": "s-list"},
    {"label": "Long List", "value": "l-list"},
    {"label": "Haiku", "value": "haiku"},
    {"label": "Sonnet", "value": "sonnet"},
    {"label": "Limerick", "value": "limerick"},
    {"label": "Rap", "value": "rap"},
    {"label": "Shakespeare", "value": "shakespeare"},
]

def headline_bot_message(message, is_user=True, is_temp=False):
    if is_temp:
        return html.Div(
            id="hl-bot-temp-message",
            className="hl-bot-message bot",
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
        className=f"hl-bot-message {'user' if is_user else 'bot'}",
        children=[
            html.Div(
                className=f"hl-bot-message-content {'user' if is_user else 'bot'}",
                children=message,
            )
        ]
    )

def get_analysis(initial_message):
    return html.Div(
        id="newsfeed-nlp",
        className="newsfeed-nlp",
        children=[
            html.Div(
                id="headline-bot",
                className="headline-bot",
                children=[
                    html.Div(
                        id="headline-bot-message-space",
                        className="headline-bot-message-space",
                        children=[
                            html.Div([], style={"flexGrow": "1"}),
                            headline_bot_message(initial_message, False),
                        ]
                    ),
                    html.Div(
                        id="headline-bot-params",
                        className="headline-bot-params",
                        children=[
                            dbc.Input(
                                id="headline-bot-query",
                                className="headline-bot-query",
                                placeholder="Enter your question here",
                                value="",
                                persistence=False,
                            ),
                            html.Button(
                                id="headline-bot-btn",
                                className="headline-bot-btn disabled",
                                disabled=True,
                                children=[
                                    html.I(className="bi bi-send-fill"),
                                ]
                            )
                        ]
                    ),
                ],
            ),
            html.Div(
                id="article-summariser",
                className="article-summariser",
                children=[
                    html.Div(
                        id="article-summariser-output",
                        className="article-summariser-output",
                        children=[
                            dcc.Loading(
                                color="#780000",
                                children=[
                                    dbc.Textarea(
                                        id="article-summariser-output-content",
                                        className="article-summariser-output-content",
                                        value="",
                                        draggable=False,
                                        readOnly=True,
                                        placeholder="Create a summary of today's headlines"
                                    ),
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        id="article-summariser-params",
                        className="article-summariser-params",
                        children=[
                            dbc.Select(
                                id="summary-method-select",
                                className="summary-method-select",
                                placeholder="Format",
                                value="",
                                options=summary_methods
                            ),
                            html.Button(
                                id="article-summariser-btn",
                                disabled=True,
                                className="article-summariser-btn disabled",
                                children="Summarise",
                            ),
                            html.Button(
                                id="download-summary-btn",
                                disabled=True,
                                className="article-summariser-btn disabled",
                                children="Download",
                            ),
                            dcc.Download(id="download-headline-summary"),
                            html.Button(
                                id="clear-summary-btn",
                                disabled=True,
                                className="article-summariser-btn disabled",
                                children="Clear",
                            ),
                        ]
                    ),
                ]
            ),
        ]        
    )