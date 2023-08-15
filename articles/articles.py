# Third-Party Imports
from newsapi import NewsApiClient

# Standard Imports
import os

# Top Headlines
def get_top_headlines():
    client = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
    headlines = client.get_top_headlines()
    return headlines