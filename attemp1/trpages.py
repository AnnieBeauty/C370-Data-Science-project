from newsapi import NewsApiClient

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = "0cf78a3837294333871108b6681392b0"
newsapi = NewsApiClient(api_key=api_key)

# Set the page size and page number
page_size = 100
page_number = 2

# Make the API request to get the second page of results
response = newsapi.get_everything(q='Taylor Swift', language='en', sort_by='publishedAt', page_size=page_size, page=page_number)

# Process the response...
