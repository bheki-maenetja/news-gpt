# Third-Party Imports
from dash import html, dcc
import dash_bootstrap_components as dbc

main_tabs =  dcc.Tabs(
    id="main-tabs",
    className="main-tabs",
    value="newsfeed",
    children=[
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Newsfeed",
            value="newsfeed",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Analysis",
            value="analysis",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="Semantics",
            value="semantics",
        ),
        dcc.Tab(
            className="main-tab",
            selected_className="main-tab-selected",
            label="NewsBot",
            value="newsbot",
        ),
    ]
)