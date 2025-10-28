import requests
import os
import time
from bs4 import BeautifulSoup

def scrape_blog(url: str) -> str:
    """
    Scrapes full blog content using Firecrawl API.
    Falls back to BeautifulSoup if Firecrawl fails or times out.
    """
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        raise ValueError("Firecrawl API key not found. Please set FIRECRAWL_API_KEY.")

    firecrawl_url = "https://api.firecrawl.dev/v1/scrape"

    # Try Firecrawl first
    try:
        for attempt in range(2):  # Retry up to twice
            res = requests.post(
                firecrawl_url,
                headers={"Authorization": f"Bearer {api_key}"},
                json={"url": url},
                timeout=30
            )
            data = res.json()
            if res.status_code == 200 and data.get("success"):
                content = data.get("content", "")
                if content.strip():
                    print("✅ Firecrawl success")
                    return content
            elif data.get("code") == "SCRAPE_TIMEOUT":
                print("⚠️ Firecrawl timed out, retrying...")
                time.sleep(5)
            else:
                print("❌ Firecrawl returned:", data)
                break
    except Exception as e:
        print(f"⚠️ Firecrawl error: {e}")

    # --- Fallback HTML scraping ---
    print("⚙️ Using fallback scraper (BeautifulSoup)...")
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        text = " ".join(paragraphs)
        if not text:
            raise Exception("No text found in fallback scraper.")
        print("✅ Fallback scraper succeeded")
        return text[:8000]  # limit to avoid GPT input length issues
    except Exception as e:
        raise Exception(f"Both Firecrawl and fallback scraper failed: {e}")
