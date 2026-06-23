import json
import os
from dotenv import load_dotenv
from pathlib import Path
from upstash_redis import Redis

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

redis = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN")
)

STORAGE_KEY = "seen_tenders"

def load_seen_data():
    data = redis.get(STORAGE_KEY)
    if data:
        return json.loads(data)
    return {}

def load_seen():
    return set(load_seen_data().keys())

def save_seen(tenders_list):
    existing = load_seen_data()
    for t in tenders_list:
        existing[t["id"]] = {
            "title":     t["title"],
            "published": t["published"],
            "closing":   t["closing"],
            "link":      t["link"]
        }
    redis.set(STORAGE_KEY, json.dumps(existing))