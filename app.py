# Third-Party Imports
from dash import Dash, html, dcc, no_update, ctx
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Standard Library Imports
# Local Imports
from user_interface.main_nav import main_nav
from user_interface.newsfeed import get_newsfeed, get_news_cards
from user_interface.analysis import get_analysis, headline_bot_message
from user_interface.keywords import get_keywords
from user_interface.semantics import get_semantics
from user_interface.editorial import get_editorial
from user_interface.newsbot import  get_newsbot

from articles.articles import get_articles, load_articles, get_cat_and_country, set_cat_and_country

from nlp.nlp import summarise_headlines, headline_chatbot, get_word_cloud

# Global Variables
app = Dash(
    name=__name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.BOOTSTRAP, 
        dbc.icons.FONT_AWESOME,
    ]
)

app.title = "NewsGPT"

server = app.server

INITIAL_HL_BOT_MESSAGE = "Ask me anything and I'll use today's headlines to find the answer."

category, country = get_cat_and_country()
get_articles(category, country)
articles = load_articles()

# UI Layout
## Main App Layout
app.layout = html.Div(
    id="main-container",
    className="main-container", 
    children=[
        dcc.Store(id="headline-bot-query-temp"),
        main_nav,
        html.Div(
            id="section-container", 
            className="section-container",
            children=[
                get_newsfeed(articles, category, country)
            ]
        ),
        html.Div(id='reload-handler-0', style={"display": "hidden"}),
        html.Div(id='reload-handler-1', style={"display": "hidden"}),
        html.Div(id='reload-handler-2', style={"display": "hidden"}),
        html.Div(id='reload-handler-3', style={"display": "hidden"}),
        html.Div(id='reload-handler-4', style={"display": "hidden"}),
        html.Div(id='reload-handler-5', style={"display": "hidden"}),
        html.Div(id='dummy', style={"display": "hidden"}),
    ]
)

## Major Components
### Section Selector
def section_selector(s_name):
    if s_name == "analysis":
        return get_analysis(INITIAL_HL_BOT_MESSAGE)
    elif s_name == "word-cloud":
        return get_keywords()
    elif s_name == "semantics":
        return get_semantics()
    elif s_name == "editorial":
        return get_editorial()
    elif s_name == "newsbot":
        return get_newsbot()

# Callback functions
"""
Callback Basics
---------------
Callbacks are a way of retrieving the values of UI components; e.g. the text
inside a form or the numerical value of a slider. Callbacks functions are 
automatically called whenever an input UI component's property changes, in 
order to update some property in another UI component (the output).
Syntax guide
------------
@app.callback(...) <-- function decorator containing all of the input and
                       output UI components.
Input(component-id, property) <-- this selects a given UI component by its ID
                                  and reads the value of the chosen property
                                  into the function. This is used as a trigger
                                  for your callback function run; when the value
                                  of 'property' in this UI component changes the
                                  function will be called.
State(component-id, property) <-- this works just like Input(component-id, property).
                                  the only difference is that this will not trigger
                                  your callback function. This is useful when you just
                                  want to get the value of a UI component property
                                  without changing the value of the property.
Output(component-id, property) <-- this selects a given UI component by its ID
                                   and changes the value of the selected property
                                   to whatever value was output by the callback
                                   function.
IMPORTANT: the order in which you specify input and output UI components is
           crucial. Always specify the output components before the input
           components. And always make sure that there is atleast 1 output
           component and at least 1 input component in the style Input(id, prop).
           If you don't do this, your callback function will not work.
In order to fully understand what each callback function does you can look at 
the ids of the UI components specified in @app.callback() and then find those 
components in the part of the code where those UI components are created.
For more info on how callback functions work you can visit the following links:
    * https://dash.plotly.com/basic-callbacks
    * https://dash.plotly.com/sharing-data-between-callbacks
    * https://dash.plotly.com/advanced-callbacks
"""
## Page Refresh Callback
@app.callback(
    Output("newsfeed-nlp-container", "children"),
    inputs=dict(
        children=(
            Input("reload-handler-0", "children"), 
            Input("reload-handler-1", "children"), 
            Input("reload-handler-2", "children"),
            Input("reload-handler-3", "children"),
            Input("reload-handler-4", "children"),
            Input("reload-handler-5", "children"),      
        ),
        tab_value=State("main-tabs", "value"),
    )
)
def refresh_page(tab_value, children):
    return section_selector(tab_value)

## Navigation Callbacks
@app.callback(
    Output("reload-handler-0", "children"),
    Input("main-tabs", "value"),
)
def main_tabs_handler(value): return None

## Newsfeed Callbacks
@app.callback(
    Output("newsfeed-articles", "children"),
    Input("category-select", "value"),
    Input("country-select", "value"),
    supress_callback_exceptions=True,
    prevent_initial_call=True,
)
def category_country_handler(category, country):
    get_articles(category, country)
    new_articles = load_articles()
    set_cat_and_country(category, country)
    return get_news_cards(new_articles)

## Analysis Callbacks
### Headline Chatbot
@app.callback(
    Output("headline-bot-btn", "disabled"),
    Output("headline-bot-btn", "className"),
    Input("headline-bot-query", "value"),
    suppress_callback_exceptions=True,
    prevent_initial_call=True,
)
def headline_bot_query_handler(query):
    if query.strip() != "":
        return False, "headline-bot-btn"
    return True, "headline-bot-btn disabled"

@app.callback(
    Output("headline-bot-message-space", "children"),
    Output("headline-bot-query-temp", "data"),
    Output("headline-bot-query", "value"),
    State("headline-bot-query", "value"),
    Input("headline-bot-btn", "n_clicks"),
    Input("headline-bot-message-space", "children"),
    suppress_callback_exceptions=True,
    prevent_initial_call=True,
)
def headline_bot_user_message_handler(query, n_clicks, current_state):
    if n_clicks is None: return current_state, "", query
    user_message = headline_bot_message(query)
    temp_message = headline_bot_message(query, False, True)
    return current_state + [user_message, temp_message], query, ""

@app.callback(
    Output("hl-bot-temp-message", "children"),
    Output("hl-bot-temp-message", "id"),
    State("headline-bot-query-temp", "data"),
    Input("headline-bot-message-space", "children"),
    suppress_callback_exceptions=True,
)
def headline_bot_system_message_handler(query, current_state):
    headlines = load_articles()
    if headlines.empty:
        return html.Div(
            className="hl-bot-message-content bot",
            children="NO ARTICLES AVAILABLE — PLEASE TRY AGAIN",
        ), ""

    new_message = headline_chatbot(headlines, query)

    return html.Div(
        className="hl-bot-message-content bot",
        children=new_message,
    ), ""

### Headline Summariser
@app.callback(
    Output("article-summariser-output-content", "value"),
    State("summary-method-select", "value"),
    Input("article-summariser-btn", "n_clicks"),
    Input("clear-summary-btn", "n_clicks"),
    suppress_callback_exceptions=True,
    prevent_initial_call=True,
    allow_duplicate=True,
)
def headline_summary_handler(sum_format, sum_clicks, clear_clicks):
    if (sum_clicks is not None or clear_clicks is not None) and sum_format != "":
        triggered_id = ctx.triggered_id
        if triggered_id == "article-summariser-btn":
            headlines = load_articles()
            if headlines.empty:
                return "NO ARTICLES — NOTHING TO SUMMARISE"
            summary = summarise_headlines(headlines, sum_format)
            return summary
        elif triggered_id == "clear-summary-btn":
            return ""

@app.callback(
    Output("article-summariser-btn", "disabled"),
    Output("article-summariser-btn", "className"),
    Output("download-summary-btn", "disabled"),
    Output("download-summary-btn", "className"),
    Output("clear-summary-btn", "disabled"),
    Output("clear-summary-btn", "className"),
    Input("summary-method-select", "value"),
    Input("article-summariser-output-content", "value"),
)
def summary_method_select_handler(sum_format, summary_content):
    return (
        sum_format == "",
        f"article-summariser-btn {'disabled' if sum_format == '' else ''}",
        summary_content == "",
        f"article-summariser-btn {'disabled' if summary_content == '' else ''}",
        summary_content == "",
        f"article-summariser-btn {'disabled' if summary_content == '' else ''}",
    )

@app.callback(
    Output("download-headline-summary", "data"),
    State("article-summariser-output-content", "value"),
    Input("download-summary-btn", "n_clicks"),
)
def download_headline_summary_handler(summary_content, n_clicks):
    if n_clicks is not None:
        return dict(content=summary_content, filename="Headline Summary.txt")

## Keywords Callback
@app.callback(
    Output("word-cloud-plot", "children"),
    Input("word-cloud-btn", "n_clicks"),
    suppress_callback_exceptions=True,
    prevent_initial_call=True,
)
def word_cloud_headline(n_clicks):
    if n_clicks is not None:
        headlines = load_articles()
        if headlines.empty:
            return html.H1("Error — No articles available")
        word_cloud = get_word_cloud(headlines)
        return html.Img(src=word_cloud)

# Running server
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")