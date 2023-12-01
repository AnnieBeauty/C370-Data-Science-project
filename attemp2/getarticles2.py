import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from dotenv import load_dotenv
import json

# Load API key from .env file
load_dotenv()
api_key = os.getenv('NEWS_API_KEY')

# Initialize NewsApiClient with the API key
newsapi = NewsApiClient(api_key=api_key)

def get_articles_by_source(source, num_articles=100):
    # Get articles about Taylor Swift from the past month
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    response = newsapi.get_everything(
        q='Taylor Swift',
        sources=source,
        from_param=start_date.strftime('%Y-%m-%d'),
        to=end_date.strftime('%Y-%m-%d'),
        language='en',
        sort_by='publishedAt',
        page_size=num_articles
    )

    if response['status'] == 'ok':
        return response['articles']
    else:
        print(f"Error: {response['message']}")
        return []

def load_articles_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_articles_to_json(articles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(articles, file, indent=2)

if __name__ == "__main__":
    # List of known sources related to Taylor Swift
    total = 0
    with open('us_sources_cache.json', 'r') as us_file:
        us_sources_data = json.load(us_file)

    with open('ca_sources_cache.json', 'r') as ca_file:
        ca_sources_data = json.load(ca_file)

    # Step 1.2: Extract the list of US and Canadian sources

    ca_sources2 = [source['id'] for source in ca_sources_data]
    us_sources2 = [source['id'] for source in us_sources_data]

    taylor_swift_sources = ca_sources2 + us_sources2


    # Directory to save JSON files
    output_directory = 'output'

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for source in taylor_swift_sources:
        # Check if a cached file exists for the source
        cache_filename = os.path.join(output_directory, f'{source}_taylor_swift_articles.json')
        cached_articles = load_articles_from_file(cache_filename)

        if cached_articles:
            print(f"Using cached articles for {source}")
            articles = cached_articles

        else:
            # Get articles for each source
            articles = get_articles_by_source(source)

            # Save articles to a cached JSON file
            save_articles_to_json(articles, cache_filename)
            print(f"Articles from {source} saved to {cache_filename}")
        print("collected " + str(len(articles)))
        total += len(articles)
        print("total = " + str(total))
        # Process the articles as needed...
