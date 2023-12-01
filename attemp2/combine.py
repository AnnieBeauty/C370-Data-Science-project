import os
import json

def combine_articles(input_directory, output_filename):
    # Initialize an empty list to store combined articles
    combined_articles = []

    # Iterate through each JSON file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            file_path = os.path.join(input_directory, filename)

            # Load articles from the current file
            with open(file_path, 'r', encoding='utf-8') as file:
                articles = json.load(file)

            # Extend the list of combined articles with the articles from the current file
            combined_articles.extend(articles)

    # Save the combined articles to a new JSON file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        json.dump(combined_articles, output_file, indent=2)
        print(len(combined_articles))


if __name__ == "__main__":
    # Directory containing individual JSON files
    input_directory = 'output'

    # Output file for combined articles
    output_filename = 'combined_articles.json'

    # Combine articles from the input directory into a single file
    combine_articles(input_directory, output_filename)

    print(f"Combined articles saved to: {output_filename}")
