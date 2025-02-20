import feedparser

"""
This script reads RSS feeds from different news sources and stores the articles in a list.
A for loop iterates over the RSS_URL list and reads the RSS feed using the feedparser library.
The entries are stored in the posts list.

"""

RSS_URL = ['http://www.dn.se/nyheter/m/rss/',
           'https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/', 
           'https://feeds.expressen.se/nyheter/',
           'http://www.svd.se/?service=rss', 
           'http://api.sr.se/api/rss/program/83?format=145',
           'http://www.svt.se/nyheter/rss.xml']

posts = []

for url in RSS_URL:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        posts.append(entry)

print(posts)


