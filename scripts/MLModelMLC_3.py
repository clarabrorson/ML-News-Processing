"""
This script is used to train a multi-label classification model using a Naive Bayes classifier.
The model is trained on a dataset containing text data and the labels are binary.
The script uses a pipeline to train the model and GridSearchCV to find the best hyperparameters.
The script also calculates the accuracy of the model on a test set.
The script outputs the best score, best parameters, best estimator and accuracy of the model.

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
from sklearn.naive_bayes import MultinomialNB


nltk.data.path.append('C:/Users/clara/AppData/Roaming/nltk_data')

if not sys.warnoptions:
    warnings.simplefilter("ignore")

data_path = "C:/Users/clara/ML/Book1.csv"
data_raw = pd.read_csv(data_path)

data_raw = data_raw.sample(frac=1)

categories = list(data_raw.columns.values)
categories = categories[2:] 

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

train, test = train_test_split(data_raw, random_state=42, test_size=0.30, shuffle=True)
train_text = train['Heading']
test_text = test['Heading']

vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
vectorizer.fit(train_text)

x_train, x_test = vectorizer.transform(train_text), vectorizer.transform(test_text)
y_train, y_test = train.drop(columns=['Id', 'Heading']), test.drop(columns=['Id', 'Heading'])

NB_pipeline = Pipeline([
    ('clf', OneVsRestClassifier(MultinomialNB()))
])


param_grid = {
    'clf__estimator__alpha': [0.1, 0.5, 1.0, 5.0, 10.0] 
}

grid = GridSearchCV(NB_pipeline, param_grid, cv=5, scoring='accuracy')
grid.fit(x_train, y_train)

print("Best score: ", grid.best_score_)
print("Best params: ", grid.best_params_)
print("Best estimator: ", grid.best_estimator_)

best_clf_pipeline = grid.best_estimator_
best_clf_pipeline.fit(x_train, y_train)


y_pred_proba = best_clf_pipeline.predict_proba(x_test)
threshold = 0.3 
y_pred = (y_pred_proba >= threshold).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

categories = categories
x_train = x_train
vectorizer = vectorizer
best_clf_pipeline = best_clf_pipeline
