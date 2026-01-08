import urllib.parse

def amazon_search(page, query):
    print("🟢 Amazon adapter (URL-based, stable)")

    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.amazon.in/s?k={encoded}"

    page.goto(url, wait_until="domcontentloaded")
