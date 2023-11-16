import unittest
from datetime import datetime, timedelta
import datetime
from newscover.newsapi import fetch_latest_news

api_key = "yourkey"

class NewsAPITests(unittest.TestCase):

    def test_no_keywords_provided(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key="YOUR_API_KEY", news_keywords="")

    def test_lookback_days(self):
        #api_key = "YOUR_API_KEY"
        news_keywords = "example"
        lookback_days = 10  # Set your desired lookback period

        articles = fetch_latest_news(api_key, news_keywords, lookback_days)

        today = datetime.datetime.now()
        oldest_allowed_date = today - datetime.timedelta(days=lookback_days)

        for article in articles:
            published_at = datetime.datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
            self.assertTrue(published_at >= oldest_allowed_date)

    def test_non_alphabetic_character_in_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(api_key=api_key, news_keywords="inval!d_keyword")


if __name__ == '__main__':
    unittest.main()
