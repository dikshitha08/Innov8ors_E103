def generic_search(page, query):
    print("🟡 Generic adapter")
    box = page.locator("input").first
    box.fill(query)
    page.keyboard.press("Enter")
