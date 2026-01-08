import sys
from browser import launch_browser
from agent.intent_parser import parse_intent
from agent.router import route

if len(sys.argv) < 3:
    print("Usage: py main.py <url> <command>")
    exit()

url = sys.argv[1]
command = " ".join(sys.argv[2:])

browser, page = launch_browser()
page.goto(url, wait_until="domcontentloaded")

print("🧠 Parsing intent...")
intent_data = parse_intent(command)
print("📦 Intent:", intent_data)

route(page, url, intent_data["intent"], intent_data["query"])

input("🔵 Press ENTER to close browser")
browser.close()
