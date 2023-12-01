import json

def load_articles_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_articles_to_file(file_path, articles):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(articles, file, indent=2)
        print(len(articles))

def find_unique_articles(file1_path, file2_path, output_path):
    # Load articles from both files
    articles_file1 = load_articles_from_file(file1_path)
    articles_file2 = (load_articles_from_file(file2_path))['articles']

    # Find articles in file2 that are not in file1
    #unique_articles = []
    unique_articles = [article for article in articles_file1 if article not in articles_file2]

    # Save the unique articles to the output file
    save_articles_to_file(output_path, unique_articles)

if __name__ == "__main__":
    # Replace these file paths with the actual paths of your files
    file1_path = 'combined_articles.json'
    file2_path = 'filtered_news_stories2.json'
    output_path = 'output_file.json'

    # Find and save unique articles
    find_unique_articles(file1_path, file2_path, output_path)

    print(f"Unique articles saved to: {output_path}")
