# Analysis of ML-News-Processing

## Overview
This project is based on a previous project where I experimented with different classifiers to achieve the highest accuracy. The classifier model that performed the best was then used in this project to classify news articles fetched from various RSS feeds.

## Classifier Selection
During the experimentation phase, I tested multiple classifiers to determine which one would provide the highest accuracy for classifying news articles. The best performing classifier was a `OneVsRestClassifier` with a `MultinomialNB` estimator and an alpha parameter of 0.1.

### Experimentation Results
The following results were obtained during the experimentation phase:

- **Best Score:** 0.20730417593278974
- **Best Parameters:** {'clf__estimator__alpha': 0.1}
- **Best Estimator:** `Pipeline(steps=[('clf', OneVsRestClassifier(estimator=MultinomialNB(alpha=0.1)))])`

The accuracy of the selected classifier on the test data was 0.3737704918032787.

## Implementation in ML-News-Processing
The selected classifier model was integrated into the ML-News-Processing project to classify news articles fetched from various RSS feeds. The following steps were performed:

1. **Fetching RSS Feeds:** The `scripts/RssArticles_1.py` script was used to fetch news articles from various RSS feeds.
2. **Extracting Information:** The `scripts/FullRSSList_1_2.py` script was used to extract necessary information from the fetched articles.
3. **Training the Model:** The `scripts/MLModelMLC_3.py` script was used to train the multi-label classification model using the selected classifier.
4. **Classifying Articles:** The `scripts/MLModelReturns_4.py` script was used to classify the articles using the trained model.

### Example Output
Here is an example of the output obtained during the classification process:

- **Classified Article:**
  ```json
  {
    "title": "Misstänkta för Liam Paynes död släppta",
    "summary": "Tre personer som åtalats för dråp i samband med One Direction-stjärnan Liam Paynes död är inte längre misstänkta.",
    "link": "https://www.dn.se/kultur/misstankta-for-liam-paynes-dod-slappta/",
    "published": "Thu, 20 Feb 2025 10:09:23 +0100",
    "topics": ["SamhalleKonflikter"]
  }

    
## Future Work

- **Improving Accuracy:** Further experimentation can be done to improve the accuracy of the classifier model by tuning hyperparameters or trying different classifiers.
- **Enhancing Features:** Additional features can be extracted from the news articles to improve the classification accuracy.
- **Enhancing User Interface:** A user interface can be developed to allow users to interact with the system and view the classified news articles.

