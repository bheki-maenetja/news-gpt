# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_news_card():
    return dbc.Card(
        id="",
        class_name="news-card",
        children=[
            dbc.CardImg(src="/assets/placeholder.jpg", top=True),
            dbc.CardBody(
                children=[
                    html.P("News article headline"),
                    html.Hr(),
                    html.P("News article description"),
                ]
            ),
        ]
    )

def get_newsfeed():
    return html.Div(
        id="newsfeed-section",
        className="newsfeed-section",
        children=[
            html.Div(
                id="main-article-feed",
                className="main-article-feed",
                children=[
                    get_news_card()
                    for _ in range(100)
                ]
            ),
            html.Div(
                id="newsfeed-nlp",
                className="newsfeed-nlp",
                children=[
                    html.H2("Summariser and chatbot"),
                ]
            )
        ]
    )