# ML-News-Processing

## Overview
ML-News-Processing is a project that processes news articles from various RSS feeds, classifies them using a machine learning model, and displays them on a Streamlit web application. The project includes scripts for fetching RSS feeds, training a machine learning model, classifying articles, and displaying the results on a web interface.

## Project Structure
ML-News-Processing/ ├── .gitignore ├── main.py ├── README.md ├── scripts/ │ ├── DbTransfer_5.py │ ├── FullRSSList_1_2.py │ ├── MLModelMLC_3.py │ ├── MLModelReturns_4.py │ ├── RssArticles_1.py │ └── RssFeedNewArticle_2.py └── web/ ├── app.py ├── config.py ├── db.py ├── news.jpg └── ui.py

## Setup
1. Clone the repository:
    ```sh
    git clone <https://github.com/clarabrorson/ML-News-Processing>
    cd ML-News-Processing
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a MySQL database in your local environment and update the database credentials in the  file.
    ```sh
    DB_CONFIG = {
    "host": "localhost",
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "database": "news"
    }
    ```
## Usage
1. Fetch RSS feeds and classify articles:
    - Run `scripts/RssArticles_1.py` to fetch RSS feeds and store articles.
    - Run `scripts/FullRSSList_1_2.py` to extract necessary information from RSS feeds.
    - Run `scripts/MLModelMLC_3.py` to train a multi-label classification model.
    - Run `scripts/MLModelReturns_4.py` to classify articles using the trained model.

2. Transfer classified articles to the database:
    - Run `scripts/DbTransfer_5.py` to transfer classified articles to the MySQL database.

3. Run the Streamlit web application:
    - Run `web/app.py` using Streamlit to start the web application.

## Scripts
- : Fetches RSS feeds and stores articles.
- : Extracts necessary information from RSS feeds.
- : Trains a multi-label classification model.
- : Classifies articles using the trained model.
- : Transfers classified articles to the MySQL database.

## Web Application
The web application is built using Streamlit and includes the following files:
- : Main file for the Streamlit web application.
- : Contains database configuration.
- : Fetches data from the MySQL database.
- : Displays the news articles on the web interface.

## License
This project is licensed under the MIT License.