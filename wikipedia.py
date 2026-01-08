def wikipedia_search(page, query):
    print("🟢 Wikipedia adapter")
    search = page.locator("#searchInput")
    search.fill(query)
    page.keyboard.press("Enter")
    page.wait_for_load_state("domcontentloaded")
