rss_feeds = {
    "Dev.to": "https://dev.to/feed",
    "Le Monde Tech": "https://www.lemonde.fr/pixels/rss_full.xml",
    "Numerama": "https://www.numerama.com/feed",
    "ZDNet France": "https://www.zdnet.fr/feeds/rss/actualites",
    "01net Actu": "https://www.01net.com/rss/actualites",
    "Bloomberg Technology": "https://www.bloomberg.com/technology.rss",
    "Hacker News": "https://news.ycombinator.com/rss",
}

import requests
import feedparser

# Fonction pour récupérer les articles RSS
def get_rss_feed(url, num_articles=5):
    headers = {"User-Agent": "Mozilla/5.0"}  # Pour contourner les restrictions de certains sites
    response = requests.get(url, headers=headers)
    feed = feedparser.parse(response.content)
    return [(entry.title, entry.link) for entry in feed.entries[:num_articles]]

# Récupération des articles RSS
rss_news = {}
for name, url in rss_feeds.items():
    rss_news[name] = get_rss_feed(url, num_articles=3)

# Affichage des résultats
print("\n🌐 Actus RSS:")
for source, articles in rss_news.items():
    print(f"\n🔹 {source}:")
    for title, link in articles:
        print("-", title, "👉", link)
