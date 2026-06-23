# 🔔 MahaTenders Discord Alert Bot

A lightweight Python automation tool that monitors [MahaTenders.gov.in](https://mahatenders.gov.in/nicgep/app) for new and updated tenders and sends real-time alerts to a Discord channel — no browser automation needed, runs entirely on free cloud services.

---

## Features

- Scrapes live tender data from MahaTenders using `requests` + `BeautifulSoup`
- Detects **new tenders** and **updated tenders** (e.g. closing date changes)
- Sends formatted Discord alerts with title, published date, closing date, and direct link
- Sorts tenders by published date (newest first)
- Stores seen tenders in **Upstash Redis** so data persists between runs
- Runs automatically every 30 minutes via **Render Cron Jobs**
- No Selenium, no browser — works on any free cloud hosting service

---

## How It Works

```
Every 30 minutes
      ↓
Render wakes up and runs main.py
      ↓
scraper.py fetches MahaTenders HTML
and extracts all tender rows
      ↓
storage.py reads seen tender IDs
from Upstash Redis
      ↓
main.py compares scraped vs seen
      ↓
New tenders → Discord alert sent
      ↓
storage.py saves updated data
back to Upstash Redis
      ↓
Render shuts down until next run
```

---

## Project Structure

```
Tender Alert/
├── main.py               # Entry point — runs the check once and exits
├── scraper.py            # Fetches and parses MahaTenders HTML
├── storage.py            # Reads and writes seen tenders to Upstash Redis
├── notifier.py           # Sends alerts to Discord via webhook
├── requirements.txt      # Python dependencies
├── .env                  # Your secrets (never push this to GitHub)
└── .gitignore            # Keeps .env out of GitHub
```

---

## Tech Stack

- **Python** — core language
- **Requests** — fetching the MahaTenders webpage
- **BeautifulSoup4** — parsing HTML to extract tender data
- **Upstash Redis** — cloud key-value store for persisting seen tenders
- **Render** — cloud cron job runner (free tier)
- **Discord Webhook** — sending formatted alerts to Discord

---

## Deploying to Render

1. Push your code to GitHub (without `.env`)
2. Go to [render.com](https://render.com) → **New** → **Cron Job**
3. Connect your GitHub repository
4. Fill in:
   - **Build Command:** `pip install -r requirements.txt`
   - **Command:** `python main.py`
   - **Schedule:** `*/30 * * * *`
5. Add your environment variables under **Environment Variables**:
   - `DISCORD_WEBHOOK_URL`
   - `UPSTASH_REDIS_REST_URL`
   - `UPSTASH_REDIS_REST_TOKEN`
6. Click **Create Cron Job**

---

## Discord Alert Format

```
🔔 NEW TENDER ALERT
━━━━━━━━━━━━━━━━━━━━━━
📄 Title: Engineering Exploration Lab Equipment Procurement List
━━━━━━━━━━━━━━━━━━━━━━
📅 Published: 09-Jun-2026 05:00 PM
⏰ Closing:   10-Jun-2026 05:00 PM
━━━━━━━━━━━━━━━━━━━━━━
🔗 Link: https://mahatenders.gov.in/...
```

Updated tenders show a 🔄 icon instead of 🔔.

---

## Author

Made by [Psn](https://github.com/src-geek07)
