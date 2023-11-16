import requests
import datetime


def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    if not news_keywords:
        raise ValueError("news_keywords cannot be empty")

    # Ensure the news_keywords contain only alphabetic characters and spaces
    if not all(keyword.isalpha() or keyword.isspace() for keyword in news_keywords):
        raise ValueError("news_keywords must contain only alphabetic characters and spaces")

    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": news_keywords,
        "language": "en",
        "from": (datetime.datetime.now() - datetime.timedelta(days=lookback_days)).strftime('%Y-%m-%d'),
        "to": datetime.datetime.now().strftime('%Y-%m-%d'),
        "apiKey": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        # Filter articles within the specified lookback period
        filtered_articles = []
        oldest_allowed_date = datetime.datetime.now() - datetime.timedelta(days=lookback_days)
        for article in articles:
            published_at = datetime.datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
            if published_at >= oldest_allowed_date:
                filtered_articles.append(article)

        return filtered_articles


    else:
        print(f"Error fetching news: {response.status_code}")
        return []
