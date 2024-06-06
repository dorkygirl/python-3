import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

# Initialize an empty queue
queue = []

def scrape(site):
    try:
        current_url = site
        r = requests.get(current_url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {current_url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        full_url = urljoin(site, href)
        if full_url.startswith(site):
            queue.append(full_url)
            print(full_url)

def queryRepeatedly():
    while True:
        try:
            # Call your scraping function here
            site = "https://www.economist.com/"
            scrape(site)
        except Exception as e:
            print(f"Exception: {e}. Restarting...")
            continue
        time.sleep(15)

if __name__ == "__main__":
    queryRepeatedly()

    









    

