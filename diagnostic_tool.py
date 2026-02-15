import requests
from bs4 import BeautifulSoup
import time

def check_website(url):
    print(f"🔍 Scanning: {url}...")
    try:
        # 1. Check Network Status
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Status: Online (200 OK)")
        else:
            print(f"❌ Status: Error ({response.status_code})")
            return

        # 2. Check for Tags (Google Analytics / Tag Manager)
        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = str(soup)
        
        tags_found = []
        if "googletagmanager" in html_content:
            tags_found.append("Google Tag Manager")
        if "UA-" in html_content or "G-" in html_content:
            tags_found.append("Google Analytics 4")
        if "adsbygoogle" in html_content:
            tags_found.append("Google Adsense")

        if tags_found:
            print(f"✅ Tags Detected: {', '.join(tags_found)}")
        else:
            print("⚠️ No Google Tags found. Client implementation might be broken.")

    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    # You can list any sites here to test
    sites = ["https://www.google.com", "https://www.example.com"]
    for site in sites:
        check_website(site)
        print("-" * 30)