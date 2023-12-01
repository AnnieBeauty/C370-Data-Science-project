import requests
import json

api_key = "0cf78a3837294333871108b6681392b0"
base_url = 'https://newsapi.org/v2/everything'

# Set common parameters
common_params = {
    'q': 'your_query',
    'apiKey': api_key,
    'pageSize': 100,  # Number of results per page
}

# Container to store all articles
all_articles = []

# Make two requests, one for each page
for page_number in range(1, 3):  # Assuming you want results from page 1 and page 2
    # Set page-specific parameter
    params = common_params.copy()
    params['page'] = page_number

    # Make the request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and use the response (response.json())
        news_data = response.json()
        articles = news_data['articles']

        # Append articles to the container
        all_articles.extend(articles)
    else:
        print(f"Error on page {page_number}: {response.status_code}")
        print(response.text)

# Save all articles to a JSON file
with open('news_data.json', 'w') as json_file:
    json.dump(all_articles, json_file, indent=2)

print("Data saved to news_data.json")
