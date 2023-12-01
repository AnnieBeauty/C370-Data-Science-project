import os
import json
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get your News API key from the environment variable
newsapi_key = os.getenv("NEWSAPI_KEY")

# Check if the API key is available
if not newsapi_key:
    raise ValueError("NEWSAPI_KEY is not set in the environment variables. Please set it in a .env file.")

# Initialize the NewsApiClient with your API key
newsapi = NewsApiClient(api_key=newsapi_key)

def get_sources(country, language="en", use_cache=True):
    """
    Get all news sources for a given country and language.

    Parameters:
    - country (str): The country code (e.g., 'us', 'ca').
    - language (str): The language of the news sources. Default is 'en'.
    - use_cache (bool): Whether to use caching. Default is True.

    Returns:
    - list: List of news sources.
    """
    cache_filename = f"{country}_sources_cache.json"

    if use_cache and os.path.exists(cache_filename):
        with open(cache_filename, "r") as cache_file:
            sources = json.load(cache_file)
    else:
        sources = newsapi.get_sources(country=country, language=language)["sources"]

        # Cache the sources
        with open(cache_filename, "w") as cache_file:
            json.dump(sources, cache_file, indent=2)

    return sources

def print_sources(sources):
    """
    Print the names of news sources.

    Parameters:
    - sources (list): List of news sources.
    """
    if not sources:
        print("No news sources found.")
        return

    print("News Sources:")
    for source in sources:
        print(f"- {source['name']} ({source['id']})")

if __name__ == "__main__":
    # Specify the countries for which you want to get news sources
    countries = ["us", "ca"]

    for country in countries:
        print(f"\nNews Sources for {country.upper()}:")
        sources = get_sources(country)
        print_sources(sources)
