# Third-Party Imports
from newsapi import NewsApiClient
import pandas as pd

# Standard Imports
import os
import json

# Getting Articles
def get_articles(category="general", country="us", save=True):
    try:
        client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
        res = client.get_top_headlines(
            category=category, 
            country=country,
            page_size=100,
        )
    except Exception as e:
        print(f"'get_articles' -> Something is wrong: {e}")
        return []
    
    if not save:
        return res["articles"]
    save_articles(res["articles"])

def search_articles(query):
    try:
        client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
        res = client.get_everything(
            q=query,
            sort_by="relevancy",
            page_size=100,
            language="en",
        )
    except Exception as e:
        print(f"'search_articles' -> Something is wrong: {e}")
        return []
    
    art_df = pd.DataFrame.from_records(res["articles"])

    return art_df

# Saving and Loading Articles
def save_articles(articles):
    try:
        articles_json = json.dumps(articles)
        with open("state/articles.json", "w") as f:
            f.write(articles_json)
    except Exception as e:
        print(f"'save_articles' -> Something  went wrong {e}")

def load_articles(refresh=False):
    if refresh:
        get_articles()

    try:
        return pd.read_json("state/articles.json", orient="records")
    except Exception as e:
        print(f"'load_articles' -> Something is wrong {e}")