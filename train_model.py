import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset with document text and corresponding categories
data = {
    'text': [
        'This product comes with a 1-year warranty...',
        'The transaction was completed successfully on...',
        'Here are the troubleshooting steps for your device...'
    ],
    'category': ['warranty', 'transaction', 'troubleshooting']
}

df = pd.DataFrame(data)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['category'], test_size=0.2)

# Text vectorization using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Save the trained model and vectorizer for later use
joblib.dump(model, 'model/text_classifier_model.pkl')
joblib.dump(vectorizer, 'model/tfidf_vectorizer.pkl')
