# Third-Party Imports
from dash import html, dcc

main_tabs = dcc.Tabs(
    id="main-tabs",
    className="main-tabs",
    value="analysis",
    children=[
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Analysis",
            value="analysis",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Keywords",
            value="word-cloud",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Editorial",
            value="editorial",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="NewsBot",
            value="newsbot",
        ),
    ]
)

main_nav = html.Div(
    id="main-nav",
    className="main-nav",
    children=[
        html.H1("NewsGPT", className="nav-header"),
        main_tabs,
    ]
)