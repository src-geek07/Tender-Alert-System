import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(tenders, label="NEW"):
    emoji = "🔔" if label == "NEW" else "🔄"
    for t in tenders:
        message = (
            f"{emoji} **{label} TENDER ALERT**\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**Title:** {t['title']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**Published:** {t['published']}\n"
            f"**Closing:**   {t['closing']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"**Link:** {t['link']}\n"
        )
        requests.post(WEBHOOK_URL, json={"content": message})   