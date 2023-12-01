import json

# Step 1: Read the JSON file containing news stories
with open('../attemp1/all_articles2.json', 'r') as file:
    news_stories = json.load(file)

# Step 1.1: Read the JSON files containing US and Canadian sources
with open('us_sources_cache.json', 'r') as us_file:
    us_sources_data = json.load(us_file)

with open('ca_sources_cache.json', 'r') as ca_file:
    ca_sources_data = json.load(ca_file)

# Step 1.2: Extract the list of US and Canadian sources
us_sources = {source['id']: source['name'] for source in us_sources_data}
ca_sources = {source['id']: source['name'] for source in ca_sources_data}
ca_sources2 = [source['id'] for source in ca_sources_data]
us_sources2 = [source['id'] for source in us_sources_data]
print(ca_sources2)
print(us_sources2)
finalsources = ca_sources2 + us_sources2
print(finalsources)
# Step 2: Extract the source information from each news story
#print(news_stories['articles'])
# filtered_stories = [story for story in news_stories if story['source']['id'] in us_sources or story['source']['id'] in ca_sources]
#
# # Save the filtered stories to a new JSON file
# with open('../attemp1/filtered_news_stories2.json', 'w') as output_file:
#     json.dump({'articles': filtered_stories}, output_file, indent=2)
#
# print("Filtered news stories saved to 'filtered_news_stories.json'")
# print(len(filtered_stories))
