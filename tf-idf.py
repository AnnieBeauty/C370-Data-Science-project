import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('Data1130.tsv', sep='\t', header=None, names=['title', 'description', 'category','signum'])
df.fillna('', inplace=True)
df = df[df['category'] != 'unrelated']

df['text'] = df['title'].astype(str) + ' ' + df['description'].astype(str)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['text'])
feature_names = vectorizer.get_feature_names_out()

categories = ['NFL', 'music', 'award', 'viral_moment', 'relationship', 'miscellaneous', 'top_chart']

with open('testing_tfidf.tsv', 'w', encoding='utf-8') as file:
    for category in categories:
        category_idx = df[df['category'] == category].index
        category_matrix = tfidf_matrix[category_idx]

        sum_scores = category_matrix.sum(axis=0)
        top_words = [(feature_names[i], sum_scores[0, i]) for i in sum_scores.argsort()[0, 10:][::-1]]
        
 
        file.write(f"Top words for {category}:\n")
        for word, score in top_words:
            file.write(f"  {word}: {score}\n")
        file.write("\n")