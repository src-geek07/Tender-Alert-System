import requests
from bs4 import BeautifulSoup

def get_tenders():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
    }

    url = "https://mahatenders.gov.in/nicgep/app"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    tenders = []

    rows = soup.select("tr.even, tr.odd")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 4:
            title_el = cols[0].find("a")
            if not title_el:
                continue

            title = title_el.get_text(strip=True)
            published = cols[2].get_text(strip=True)

            if not title or not published:
                continue

            raw_link = title_el.get("href")
            link = raw_link if raw_link.startswith("http") else "https://mahatenders.gov.in" + raw_link

            tenders.append({
                "id":        row.get("id"),
                "title":     title,
                "link":      link,
                "published": published,
                "closing":   cols[3].get_text(strip=True),
            })

    return tenders


if __name__ == "__main__":
    tenders = get_tenders()
    for t in tenders:
        print(t)