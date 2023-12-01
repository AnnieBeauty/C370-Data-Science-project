import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from dotenv import load_dotenv
import json

# Load API key from .env file
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# Check if API key is provided
if not api_key:
    raise ValueError("API key not found. Please provide your News API key in the .env file.")

# Initialize NewsApiClient
newsapi = NewsApiClient(api_key=api_key)

# Set the initial end date to 30 days ago
end_date = datetime.utcnow() - timedelta(days=30)

# List to store all articles
all_articles = []

# Loop up to 5 times or until from date is today
for iter in range(30):
    # Format dates for News API request

    formatted_from_date = (end_date + timedelta(days=iter)).strftime("%Y-%m-%d")
    formatted_end_date = (end_date + timedelta(days=iter)).strftime("%Y-%m-%d")
    # Fetch articles
    articles = newsapi.get_everything(
        q="Taylor Swift",
        language="en",
        from_param=formatted_from_date,
        to=formatted_end_date,
        sort_by="relevancy",
        page_size=100,
    )

    # Cache articles or process them as needed
    if articles["status"] == "ok" and articles["totalResults"] > 0:
        all_articles.extend(articles["articles"])
        for article in articles["articles"]:
            # Process or cache the articles here
            print(f"Title: {article['title']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"URL: {article['url']}")
            print("\n")

        # Update end_date for the next iteration
        #end_date = datetime.strptime(articles["articles"][-1]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    else:
        # No more articles or an issue with the request
        break

    # Break the loop if the from date is today
    if end_date.date() == datetime.utcnow().date():
        break

# Print the total number of articles collected
print(f"Total Articles Collected: {len(all_articles)}")

# Cache all articles into a JSON file
with open("all_articles2.json", "w", encoding="utf-8") as json_file:
    json.dump(all_articles, json_file, ensure_ascii=False, indent=4)
