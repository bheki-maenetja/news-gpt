# Third-Party Imports
from dash import html
import dash_bootstrap_components as dbc

def news_card(headline, art_url, img_url, description):
    if headline is None:
        formatted_hl = "UNTITLED"
    elif len(headline) < 101:
        formatted_hl = headline
    else:
        formatted_hl = headline[:101] + "..."

    return html.A(
        id="",
        className="news-card",
        href=art_url,
        target="_blank",
        children=[
            html.P(
                className="news-card-headline",
                children=formatted_hl,
            ),
            html.P(
                className="news-card-description",
                children=description,
            )
        ],
        style={"backgroundImage": f"url({img_url})"}
    )

def get_news_cards(articles):
    return [
        news_card(
            r["title"], 
            r["url"], 
            r["urlToImage"], 
            r["description"],
        )
        for _, r in articles.iterrows()
    ]

def get_newsfeed(articles, category, country):
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
                                value=category,
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
                                value=country,
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
                        children=get_news_cards(articles),
                    )
                ]
            ),
            html.Div(
                id="newsfeed-nlp-container", 
                className="newsfeed-nlp-container",
            ),
        ]
    )