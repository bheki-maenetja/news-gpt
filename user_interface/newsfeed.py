# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

the_link = "https://www.cnn.com/"

article_modal = dbc.Modal(
    keyboard=False,
    backdrop="static",
    is_open=False,
    children=[
        dbc.ModalHeader(
            children=[
                dbc.ModalTitle("Article Heading")
            ]
        ),
        dbc.ModalBody(
            children=[
                html.Iframe(
                    src=the_link
                )
            ]
        )
    ]
)

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

def get_newsfeed(headlines):
    return html.Div(
        id="newsfeed-section",
        className="newsfeed-section",
        children=[
            article_modal,
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
                    html.Div(
                        id="headline-bot",
                        className="headline-bot",
                        children=[
                            html.Div(
                                id="headline-bot-message-space",
                                className="headline-bot-message-space",
                                children=[
                                    html.Div([], style={"flexGrow": "1"}),
                                    headline_bot_message("Bot message", False),
                                    headline_bot_message("User message"),
                                    headline_bot_message("", is_temp=True),
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
                                        className="headline-bot-btn",
                                        disabled=False,
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
                                        placeholder="Select a Summary Format",
                                        value="",
                                        options=[
                                            {
                                                "label": "Single Paragraph",
                                                "value": "1-para",
                                            },
                                            {
                                                "label": "Multiple Paragraphs",
                                                "value": "multi-para",
                                            },
                                            {
                                                "label": "Short Essay",
                                                "value": "s-essay"
                                            },
                                            {
                                                "label": "Long Essay",
                                                "value": "l-essay",
                                            },
                                            {
                                                "label": "Short List",
                                                "value": "s-list",
                                            },
                                            {
                                                "label": "Long List",
                                                "value": "l-list",
                                            },
                                            {
                                                "label": "Haiku",
                                                "value": "haiku",
                                            },
                                            {
                                                "label": "Sonnet",
                                                "value": "sonnet",
                                            },
                                            {
                                                "label": "Rap",
                                                "value": "rap",
                                            },
                                            {
                                                "label": "Shakespeare",
                                                "value": "shakespeare",
                                            },
                                        ]
                                    ),
                                    html.Button(
                                        id="article-summariser-btn",
                                        className="article-summariser-btn",
                                        children="Create Summary",
                                    )
                                ]
                            )
                        ],
                    ),
                ]
            )
        ]
    )