import requests
from bs4 import BeautifulSoup

def discover_assets(url):
    assets = []
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("http"):
                assets.append(href)
    except Exception as e:
        print(e)
    return list(set(assets))
