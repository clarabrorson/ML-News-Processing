"""
This script is used to classify the articles from the RSS feed. It uses the ML model trained in the previous step to classify the articles.
The script reads the articles from the RSS feed, preprocesses them, and then uses the ML model to classify them.
The script then prints the classified articles to the console.

def main():
    This function reads the articles from the RSS feed, preprocesses them, and uses the ML model to classify them.
    It returns a list of dictionaries, where each dictionary represents a classified article.

if __name__ == "__main__":
    This block of code calls the main function and prints the classified articles to the console.
    
"""

import sys
import os
import jsonschema

from FullRSSList_1_2 import AllItemsX as MyTheFinalList
from MLModelMLC_3 import categories, vectorizer, best_clf_pipeline
from RssFeedNewArticle_2 import printdepositlist


def main():

    my_text = [f"{item['title']} {item['summary']}" for item in MyTheFinalList]

    my_text_no_empty = [t for t in my_text if t.strip() != ""]

    if not my_text_no_empty:
        print("No text found for classification!")
        return []

    my_text_transformed = vectorizer.transform(my_text_no_empty)

    predictions = best_clf_pipeline.predict_proba(my_text_transformed)

    threshold = 0.3
    results = [] 

    for idx, pvector in enumerate(predictions):
        predicted_categories = [
            categories[i] for i, prob in enumerate(pvector) if prob >= threshold
        ]
        results.append(predicted_categories if predicted_categories else ["Unknown Category"])


    combinedList = []
    for i, article in enumerate(MyTheFinalList):
        title, summary, link, published = article.values()
        topics = results[i] if i < len(results) else ["Unknown Category"]
        combinedList.append([title, summary, link, published, topics])

    
    key_list = ['title', 'summary', 'link', 'published', 'topics']
    finalDict = [dict(zip(key_list, v)) for v in combinedList]

    return finalDict


if __name__ == "__main__":
    validDict = main()  
    
    if validDict:
        print("Example of a classified article:", validDict[0])
        print(f"Total number of classified articles: {len(validDict)}")
    else:
        print("No articles were classified!")
