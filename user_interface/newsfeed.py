# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

def get_news_card(headline, img_url):
    formatted_hl = headline if len(headline) < 101 else headline[:101] + "..."

    return html.Div(
        id="",
        className="news-card",
        children=[
            html.P(
                id="",
                className="news-card-headline",
                children=formatted_hl,
            )
        ],
        style={"backgroundImage": f"url({img_url})"}
    )

def get_newsfeed(headlines):
    return html.Div(
        id="newsfeed-section",
        className="newsfeed-section",
        children=[
            html.Div(
                id="main-article-feed",
                className="main-article-feed",
                children=[
                    html.Div(
                        id="newsfeed-params",
                        className="newsfeed-params",
                        children=[
                            html.H2("Top Headlines"),
                            dbc.Select(
                                id="category-select",
                                class_name="category-select",
                                placeholder="Select a News Category",
                                value=None,
                                persistence=False,
                                options=[
                                    {"label": "General", "value": "general"},
                                    {"label": "Business", "value": "business"},
                                    {"label": "Technology", "value": "technology"},
                                    {"label": "Science", "value": "science"},
                                    {"label": "Health", "value": "health"},
                                    {"label": "Sports", "value": "sports"},
                                    {"label": "Entertainment", "value": "entertainment"},
                                ]
                            ),
                            dbc.Select(
                                id="country-select",
                                class_name="country-select",
                                placeholder="Select a Country",
                                value=None,
                                persistence=False,
                                options=[
                                    {"label": "United States", "value": "us"},
                                    {"label": "United Kingdom", "value": "gb"},
                                    {"label": "South Africa", "value": "za"},
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        id="newsfeed-articles",
                        className="newsfeed-articles",
                        children=[
                            get_news_card(h["title"], h["urlToImage"])
                            for h in headlines
                        ]
                    )
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