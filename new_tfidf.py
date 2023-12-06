import json
import os
import csv
import math
import re


def load_stopwords():
    # Loading stopwords that was provided in homework9. 
    # set is collection of objects where there can't be duplicate words
    stopwords = set()
    with open("stopwords.txt", 'r') as f:
        for line in f:
            stopwords.add(line.strip())
    return stopwords


def clean(text, stopwords):
    #python library that deals with regex, this removes punctuation and replaces with with space
    text = text.lower()
    text = re.sub(r'[’‘]', " ", text)  
    text = re.sub(r'[“”]', ' ', text) 
    text = re.sub(r"'", " ", text)
    text = re.sub(r'[()\[\],-.?!:;#&"]', ' ', text)

    #remove stopwords
    filtered_words = []
    for word in text.split():
        if word not in stopwords:
            filtered_words.append(word)

    text = ' '.join(filtered_words)
    return text



def calculate_tfidf(csvfile):
    # Load the stopwords
    stopwords = load_stopwords()

    # Initialize data structures
    document_word_counts = []  # List to store word counts for each document
                               # Printing the first element of this returns {'nolte': 2, 'taylor': 2, 'swift': 2, 'humiliates': 1, 'hollywood': 1, 'trounces': 1, 'leo': 1, 'flower': 2, 'moon': 2, 'eras': 1, 'tour': 1, 
                               # 'grossed': 1, '$32': 1, 'million': 2, 'humiliating': 1, 'leonardo': 1, 'di': 1, 'caprio': 1, 'killers': 1, 'debuted': 1, '$22': 1}
    
    
    document_categories = []   # List to store category for each document


    word_document_counts = {}  # Dictionary to count documents containing each word. This is for IDF
                               #print(word_document_counts['taylor']) prints 975

    # Read the CSV file
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader)  # Skip the header

    
    for row in reader:
        title_description = f"{row[0]} {row[1]}".lower()
        category = row[2]
        text = clean(title_description, stopwords).split()

        # Count word occurrences in a single document. 
        word_counts = {}
        for word in text:
           
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

         
            if word not in word_document_counts:  
                word_document_counts[word] = 1
            else:
                word_document_counts[word] += 1

        # adding tsv file rows to lists
        document_word_counts.append(word_counts)
        document_categories.append(category)

    # Calculate TF-IDF
    num_documents = len(document_word_counts)

    #this is a dictionary of dictionary
    words_by_category = {}
    for i in range(num_documents):
        category = document_categories[i]
        word_counts = document_word_counts[i]
        tfidf_scores = {}

        for word, count in word_counts.items():
            #TF = number of times a word occurs in a document
            tf = count / sum(word_counts.values())

            # log (number of documents / number of times a document contains the word)
            idf = math.log(num_documents / word_document_counts[word])
            tfidf_scores[word] = tf * idf
          

        # if category not present, add to dictionary and respective tfidf value for each word
        if category not in words_by_category:
            words_by_category[category] = tfidf_scores
       
       # if present, keep updating the tfidf values
            for word, score in tfidf_scores.items():
                if word not in words_by_category[category]:
                    words_by_category[category][word] = score
                else:
                    words_by_category[category][word] += score

    # Sort words by TF-IDF score to get top 10cle
    top_words = {}
    for category, scores in words_by_category.items():
        sorted_words = sorted(scores.items(), key=get_score, reverse=True)
        top_words[category] = sorted_words[:10]

    #print(document_word_counts[0])
    #print(document_categories[0])
    #print(word_document_counts['taylor'])
    #print(word_counts)
    #print(words_by_category.items())
    return top_words

def get_score(item):
    return item[1]

def main():
    
    # Opening our annotated tsv file. I have removed all unrelated rows.
    with open("removed_unrelated.tsv", 'r') as f:
        tfidf_scores = calculate_tfidf(f)
    # Write our results into a json file
    with open('a.json', 'w') as f:
        json.dump(tfidf_scores, f)

if __name__ == "__main__":
    main()