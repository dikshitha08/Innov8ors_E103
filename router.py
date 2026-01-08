from adapters.wikipedia import wikipedia_search
from adapters.google import google_search
from adapters.amazon import amazon_search
from adapters.generic import generic_search

def route(page, url, intent, query):
    if intent != "search":
        print("❌ Unsupported intent")
        return

    if "wikipedia.org" in url:
        wikipedia_search(page, query)

    elif "google.com" in url:
        google_search(page, query)

    elif "amazon" in url:
        amazon_search(page, query)

    else:
        generic_search(page, query)
