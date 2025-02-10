"""
MLModelReturns_4.py

This script will:
  - Import 'MyTheFinalList' from FullRSSList_1_2.py
  - Import the trained model (best_clf_pipeline) + supporting objects (categories, vectorizer, etc.) 
    from MLModelMLC_3.py
  - Use the model to predict categories for the newly fetched RSS articles.
  - Combine the predictions with the final list from 'MyTheFinalList' and possibly produce a
    validated dictionary (validDict).

Students:
 - Complete the pseudo code to transform text, get predictions,
   and merge them with the 'MyTheFinalList'.
"""

import sys
import os
import jsonschema

# Import required scripts
from FullRSSList_1_2 import AllItemsX as MyTheFinalList
from MLModelMLC_3 import categories, vectorizer, best_clf_pipeline
from RssFeedNewArticle_2 import printdepositlist

def main():
    """
    1. Retrieve the text from printdepositlist (title + summary)
    2. Transform the text into the same vectorized format as the training data
    3. Use the trained model to classify the articles
    4. Merge classifications with 'MyTheFinalList'
    5. Validate the final structured data
    """

    # 1. Retrieve the final text from 'printdepositlist' (title + summary)
    my_text = printdepositlist

    # 2. Remove empty strings from 'my_text' if necessary
    my_text_no_empty = [t for t in my_text if t.strip() != ""]

    if not my_text_no_empty:
        print("No text found for classification!")
        return []

    # 3. Transform text using the same vectorizer from training
    my_text_transformed = vectorizer.transform(my_text_no_empty)

    # 4. Use best_clf_pipeline to get probability predictions
    predictions = best_clf_pipeline.predict_proba(my_text_transformed)

    # 5. Compare each probability to a threshold to determine the predicted categories
    threshold = 0.3
    results = []  # List of classified categories per text

    for idx, pvector in enumerate(predictions):
        predicted_categories = [
            categories[i] for i, prob in enumerate(pvector) if prob >= threshold
        ]
        results.append(predicted_categories if predicted_categories else ["Unknown Category"])

    # 6. Combine 'results' with 'MyTheFinalList'
    #    Ensure that each classified text matches the corresponding item in MyTheFinalList
    combinedList = []
    for i, article in enumerate(MyTheFinalList):
        title, summary, link, published = article
        topics = results[i] if i < len(results) else ["Unknown Category"]
        combinedList.append([title, summary, link, published, topics])

    # 7. Create the final list of dictionaries
    key_list = ['title', 'summary', 'link', 'published', 'topics']
    finalDict = [dict(zip(key_list, v)) for v in combinedList]

    # 8. Validate the final dictionaries using JSON schema
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "summary": {"type": "string"},
            "link": {"type": "string"},
            "published": {"type": "string"},
            "topics": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["title", "summary", "link", "published", "topics"]
    }

    valid_list = []
    for item in finalDict:
        try:
            jsonschema.validate(instance=item, schema=schema)
            valid_list.append(item)
        except jsonschema.exceptions.ValidationError as e:
            print(f"Validation error: {e}")

    return valid_list  # Important! Returning validDict

# 9. Run the script and store results in validDict
if __name__ == "__main__":
    validDict = main()  # Ensure validDict is created by calling main()
    
    # 10. Print an example of the classified articles
    if validDict:
        print("Example of a classified article:", validDict[0])
        print(f"Total number of classified articles: {len(validDict)}")
    else:
        print("No articles were classified!")
