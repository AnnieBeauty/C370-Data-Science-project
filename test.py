import requests
from datetime import datetime, timedelta
import csv


api_key = ""
base_url = 'https://newsapi.org/v2/everything'
query = 'Taylor Swift'
page_size = 100
max_articles = 500
current_page = 1
total_results = float('inf') 

# Calculate the dates for the past month
end_date = datetime.now()
start_date = end_date - timedelta(days=30)


articles = []


while len(articles) < max_articles and len(articles) < total_results:
    params = {
        'apiKey': api_key,
        'q': query,
        'pageSize': min(100, 500 - len(articles)),  # Ensure we don't exceed the desired total
        'page': current_page,  # Calculate the appropriate page number
        'from': start_date.strftime('%Y-%m-%d'),
        'to': end_date.strftime('%Y-%m-%d'),
        'language' :'en'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles.extend(data['articles'])
    else:
        print(f"Error {response.status_code}: {response.text}")
        break

#news = []
#for i, article in enumerate (articles):
  # print(i, article['title'])

fields = ["title", "description"]

with open("article.csv", "w", newline='', encoding='utf-8') as f:
    tsv = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    tsv.writeheader()
    
    for article in articles: 
        row = {field: article[field] for field in fields if field in article}
        tsv.writerow(row)



#print(len(articles))