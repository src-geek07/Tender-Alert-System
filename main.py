import schedule
import time
from datetime import datetime
from scraper import get_tenders
from storage import load_seen, load_seen_data, save_seen
from notifier import send_discord_alert

def check_for_tenders():
    print(f"[{datetime.now().strftime('%d-%b-%Y %I:%M %p')}] Checking for new tenders...")

    seen = load_seen()
    seen_data = load_seen_data()
    tenders = get_tenders()

    new_tenders = [t for t in tenders if t["id"] not in seen]
    updated_tenders = [
        t for t in tenders
        if t["id"] in seen_data and seen_data[t["id"]]["closing"] != t["closing"]
    ]

    if new_tenders:
        new_tenders.sort(
            key=lambda t: datetime.strptime(t["published"], "%d-%b-%Y %I:%M %p"),
            reverse=True
        )
        send_discord_alert(new_tenders, label="NEW")
        print(f"  → {len(new_tenders)} new tender(s) sent to Discord!")

    if updated_tenders:
        send_discord_alert(updated_tenders, label="UPDATED")
        print(f"  → {len(updated_tenders)} updated tender(s) sent to Discord!")

    if not new_tenders and not updated_tenders:
        print("  → No changes found.")

    save_seen(tenders)

check_for_tenders()
schedule.every(30).minutes.do(check_for_tenders)

while True:
    schedule.run_pending()
    time.sleep(60)