"""
MLModelMLC_3.py

This script trains a multi-label text classification model using data from Book1.csv.
It:
  - Loads and preprocesses the data
  - Trains a LogisticRegression-based OneVsRest model with GridSearchCV
  - Prints out the best model and accuracy
  - Exposes certain variables for import into other scripts:
       categories, x_train, vectorizer, best_clf_pipeline

Important for the assignment:
 - Students can attempt to modify hyperparameters or the threshold value to see if it
   improves accuracy or better suits the data.
 - Make sure that once the model is finalized, you "export" the key objects so that
   MLModelReturns_4 can import them.

"""

import re
import sys
import warnings
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB  # ← Använder MultinomialNB istället

# If needed for your environment:
nltk.data.path.append('C:/Users/clara/AppData/Roaming/nltk_data')

# Suppress warnings for clarity
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# 1) Load the data
data_path = "C:/Users/clara/ML/Book1.csv"  # Student: adjust if your CSV is somewhere else
data_raw = pd.read_csv(data_path)

# 2) Shuffle the data
data_raw = data_raw.sample(frac=1)

# 3) Preprocessing
categories = list(data_raw.columns.values)
categories = categories[2:]  # Usually, 'Id' and 'Heading' are the first two columns

data_raw['Heading'] = (
    data_raw['Heading']
    .str.lower()
    .str.replace('[^\w\s]', '', regex=True)
    .str.replace('\d+', '', regex=True)
    .str.replace('<.*?>', '', regex=True)
)

nltk.download('stopwords')
stop_words = set(stopwords.words('swedish'))

def removeStopWords(sentence):
    return " ".join([word for word in nltk.word_tokenize(sentence) if word not in stop_words])

data_raw['Heading'] = data_raw['Heading'].apply(removeStopWords)

stemmer = SnowballStemmer("swedish")

def stemming(sentence):
    return " ".join([stemmer.stem(word) for word in sentence.split()])

# (Optional) If you want to apply stemming, uncomment the next line:
# data_raw['Heading'] = data_raw['Heading'].apply(stemming)

# 4) Split the data
train, test = train_test_split(data_raw, random_state=42, test_size=0.30, shuffle=True)
train_text = train['Heading']
test_text = test['Heading']

# 5) Vectorize
vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
vectorizer.fit(train_text)

x_train, x_test = vectorizer.transform(train_text), vectorizer.transform(test_text)
y_train, y_test = train.drop(columns=['Id', 'Heading']), test.drop(columns=['Id', 'Heading'])

# 6) Setup ML pipeline
NB_pipeline = Pipeline([
    ('clf', OneVsRestClassifier(MultinomialNB()))
])

# 7) Hyperparameter Tuning
param_grid = {
    'clf__estimator__alpha': [0.1, 0.5, 1.0, 5.0, 10.0]  # α (smoothing) för MultinomialNB
}

grid = GridSearchCV(NB_pipeline, param_grid, cv=5, scoring='accuracy')
grid.fit(x_train, y_train)

print("Best score: ", grid.best_score_)
print("Best params: ", grid.best_params_)
print("Best estimator: ", grid.best_estimator_)

best_clf_pipeline = grid.best_estimator_
best_clf_pipeline.fit(x_train, y_train)

# 8) Predict on test data
y_pred_proba = best_clf_pipeline.predict_proba(x_test)
threshold = 0.3  # Students: consider playing with different threshold values
y_pred = (y_pred_proba >= threshold).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Make sure to "expose" these objects for import:
categories = categories
x_train = x_train
vectorizer = vectorizer
best_clf_pipeline = best_clf_pipeline
