import json, os

SEEN_FILE = "seen_tenders.json"

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            data = json.load(f)
            return set(data.keys())
    return set()

def load_seen_data():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            return json.load(f)
    return {}

def save_seen(tenders_list):
    existing = load_seen_data()
    for t in tenders_list:
        existing[t["id"]] = {
            "title":     t["title"],
            "published": t["published"],
            "closing":   t["closing"],
            "link":      t["link"]
        }
    with open(SEEN_FILE, "w") as f:
        json.dump(existing, f, indent=2)