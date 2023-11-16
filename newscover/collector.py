import argparse
import json
import os
from newscover.newsapi import fetch_latest_news


def collect_news(api_key, lookback_days, input_file, output_dir):
    with open(input_file, 'r') as file:
        keyword_sets = json.load(file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for name, keywords in keyword_sets.items():
        for keyword in keywords:
            articles = fetch_latest_news(api_key, keyword, lookback_days)
            output_file = os.path.join(output_dir, f'{name}.json')
            with open(output_file, 'a', encoding='utf-8') as output:
                json.dump(articles, output, ensure_ascii=False, indent=4)
                output.write('\n')


def main():
    parser = argparse.ArgumentParser(description="News Collector CLI Tool")
    parser.add_argument("-k", "--api_key", required=True, help="NewsAPI Key")
    parser.add_argument("-b", "--lookback", type=int, default=10, help="Number of days to look back (default: 10)")
    parser.add_argument("-i", "--input_file", required=True, help="Input JSON file")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory")

    args = parser.parse_args()

    collect_news(args.api_key, args.lookback, args.input_file, args.output_dir)


if __name__ == '__main__':
    main()
