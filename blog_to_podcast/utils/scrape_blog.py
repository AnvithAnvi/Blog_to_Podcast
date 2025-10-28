import os, time, requests
from bs4 import BeautifulSoup

def scrape_blog(url: str) -> str:
    """
    Scrapes a blog with Firecrawl first; falls back to BeautifulSoup if blocked or rate-limited.
    """
    api_key = os.getenv("FIRECRAWL_API_KEY")
    firecrawl_url = "https://api.firecrawl.dev/v1/scrape"

    # --- Try Firecrawl ---
    if api_key:
        try:
            res = requests.post(
                firecrawl_url,
                headers={"Authorization": f"Bearer {api_key}"},
                json={"url": url},
                timeout=25
            )
            data = res.json()
            if res.status_code == 200 and data.get("success"):
                return data.get("content", "")
            if "detected_unusual_activity" in str(data):
                print("⚠️ Firecrawl free tier blocked — switching to fallback.")
        except Exception as e:
            print("⚠️ Firecrawl exception:", e)

    # --- Fallback: local HTML parsing ---
    print("⚙️ Using fallback scraper (BeautifulSoup)...")
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")
    text = " ".join(p.get_text() for p in soup.find_all("p"))
    return text[:8000]
