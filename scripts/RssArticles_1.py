import feedparser

RSS_URL = 'https://www.dn.se/rss/'

posts = []

for url in [RSS_URL]:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        posts.append(entry)

print(posts)

