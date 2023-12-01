import json

# Step 1: Read the JSON file containing news stories
with open('all_articles.json', 'r') as file:
    news_stories = json.load(file)

# Step 2: Filter out articles with the source name "New York Post"
filtered_stories = [story for story in news_stories['articles'] if (story['source']['name'] == 'New York Post' or story['source']['name'] == 'Rolling Stone' or story['source']['name'] == 'Rolling Stone' or story['source']['name'] == 'Us Weekly')]

# Step 3: Save the filtered stories to a new JSON file
with open('filter2.json', 'w') as output_file:
    json.dump({'articles': filtered_stories}, output_file, indent=2)

print("Filtered news stories (excluding New York Post) saved to 'filter2.json'")
