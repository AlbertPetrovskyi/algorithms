import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin
import re


def extract_and_separate_text(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        domain = urlparse(url).netloc

        headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

        headings = [re.sub(r'\s+', ' ', h.replace('\n', ' ').strip()) for h in headings if h]
        paragraphs = [re.sub(r'\s+', ' ', p.replace('\n', ' ').strip()) for p in paragraphs if p]

        result = {
            domain: {
                'headings': [h for h in headings if h],
                'paragraphs': [p for p in paragraphs if p],
                'links': links,
            }
        }

        return json.dumps(result, indent=4)
    else:
        return json.dumps({"error": "Failed to retrieve the page."})


url = "https://huggingface.co"
print(extract_and_separate_text(url))