# MahaTenders Discord Alert Bot

A Python automation tool that monitors [MahaTenders.gov.in](https://mahatenders.gov.in/nicgep/app) for new and updated tenders and sends real-time alerts to a Discord channel , sorted by date and checked every 30 minutes.

---

## Features

- Scrapes live tender data from MahaTenders using Selenium
- Detects **new tenders** and **updated tenders** (e.g. closing date changes)
- Sends formatted Discord alerts with title, published date, closing date, and direct link
- Sorts tenders by published date (newest first)
- Stores seen tenders locally so you never get duplicate alerts
- Runs automatically every 30 minutes in the background

---

## Requirements

- Python 3.8+
- Google Chrome installed
- ChromeDriver (matching your Chrome version)

### Python Libraries used

```
selenium
requests
schedule
python-dotenv
```

## How It Works

1. **Scraper** opens MahaTenders in a headless Chrome browser and finds all tender rows
2. **Storage** compares scraped tenders against `seen_tenders.json`
3. **New tenders** — IDs not in the file — trigger a 🔔 NEW TENDER ALERT
4. **Updated tenders** — same ID but changed closing date — trigger a 🔄 UPDATED TENDER ALERT
5. All current tenders are saved to `seen_tenders.json` for the next check

---

## Discord Alert Format

```
NEW TENDER ALERT
━━━━━━━━━━━━━━━━━━━━━━
Title: Engineering Exploration Lab Equipment Procurement List
━━━━━━━━━━━━━━━━━━━━━━
Published: 09-Jun-2026 05:00 PM
Closing:   10-Jun-2026 05:00 PM
━━━━━━━━━━━━━━━━━━━━━━
Link: https://mahatenders.gov.in/...
```

---

## Changing the Check Interval

In `main.py`, find this line:

```python
schedule.every(30).minutes.do(check_for_tenders)
```

Change `30` to however many minutes you want between checks.

---

## Notes

- The site blocks direct HTTP requests, so Selenium (real browser) is required
- `seen_tenders.json` is auto-created on first run — do not delete it after setup
- Add `seen_tenders.json` and `.env` to `.gitignore` before pushing to GitHub

---

## Author

Made by [Psn](https://github.com/src-geek07)
