import json
import csv

# Step 1: Read the filtered JSON file
with open('output_file.json', 'r') as file:
    filtered_stories_data = json.load(file)

# Step 2: Extract relevant information and prepare data for TSV
data_for_tsv = []
for story in filtered_stories_data:
    title = story.get('title', '')
    description = story.get('description', '')

    # You may adjust the following line to include additional information or topics if available
    data_for_tsv.append([title, description, '', ''])

# Step 3: Write data to a TSV file
headers = ['title', 'description', 'topic', 'signum']

with open('annotated_data2.tsv', 'w', newline='', encoding='utf-8') as tsv_file:
    tsv_writer = csv.writer(tsv_file, delimiter='\t')

    # Write headers
    tsv_writer.writerow(headers)

    # Write data
    tsv_writer.writerows(data_for_tsv)

print("TSV file 'annotated_data.tsv' created successfully.")
