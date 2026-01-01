import requests
from bs4 import BeautifulSoup

def fetch_jd_from_url(url):
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            raise Exception(f"Status code {resp.status_code}")

        soup = BeautifulSoup(resp.text, "html.parser")
        # Extract main text content
        main_text = ""
        for tag in soup.find_all(["p", "li"]):
            main_text += tag.get_text(separator=" ", strip=True) + "\n"

        if len(main_text.strip()) == 0:
            raise Exception("No text extracted from page")

        return main_text.strip()

    except Exception as e:
        print(f"⚠️ Could not fetch JD from URL: {e}")
        return None
