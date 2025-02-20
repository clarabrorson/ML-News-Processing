
from RssArticles_1 import posts
from datetime import datetime

"""
This script is used to extract the necessary information from the RSS feed and create a list of lists with the information.
The list of lists will be used to create a dataframe in the next script.

AllItemsX: A list of dictionaries with the necessary information from the RSS feed.
ThefinalList: A list of lists with the necessary information from the RSS feed.
MyTheFinalList: The list of lists that will be used to create a dataframe in the next script.

"""

def gettingNecessaryList():
    
    allitems = []
    
    for post in posts:
        try:
            tempdict = {
                "title": post.get("title", ""),
                "summary": post.get("summary", ""),
                "link": post.get("link", ""),
                "published": post.get("published", "")
            }
            allitems.append(tempdict)
        except Exception as e:
            print(f"Fel vid extrahering: {e}")

    
    return allitems

AllItemsX = gettingNecessaryList()

def ThefinalList():
    
    finalList = []

    for item in AllItemsX:
        title, summary, link, published = item.values()
        try:
            published_date = datetime.strptime(published, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            published_date = "Unknown"
        finalList.append([title, summary, link, str(published_date)])
    
    return finalList

MyTheFinalList = ThefinalList()

print(MyTheFinalList)
print(len(MyTheFinalList))