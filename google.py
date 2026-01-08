def google_search(page, query):
    print("🟢 Google adapter (URL-based, stable)")

    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded}"

    page.goto(url, wait_until="domcontentloaded")
