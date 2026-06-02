from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_tenders():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://mahatenders.gov.in/nicgep/app")
    
    tenders = []
    rows = driver.find_elements(By.CSS_SELECTOR, "tr.even, tr.odd")
    
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 4:
            try:
                title_el = cols[0].find_element(By.TAG_NAME, "a")
                title = title_el.text.strip()
                published = cols[2].text.strip()
                
                if not title or not published:
                    continue
                
                raw_link = title_el.get_attribute("href")
                link = raw_link if raw_link.startswith("http") else "https://mahatenders.gov.in" + raw_link
                
                tenders.append({
                    "id":        row.get_attribute("id"),
                    "title":     title,
                    "link":      link,
                    "published": published,
                    "closing":   cols[3].text.strip(),
                })
            except:
                continue
    
    driver.quit()
    return tenders


if __name__ == "__main__":
    tenders = get_tenders()
    for t in tenders:
        print(t)
        
