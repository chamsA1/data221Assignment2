from bs4 import BeautifulSoup
import requests


def get_page_title(url):

    # Get webpage (pretend to be a browser)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("title")

    return title_tag.text


def get_first_paragraph(url):

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", id="mw-content-text")

    paragraphs = content_div.find_all("p")

    for paragraph in paragraphs:

        text = paragraph.text.strip()

        if len(text) >= 50:
            return text


url = "https://en.wikipedia.org/wiki/Data_science"

print("Page Title:")
print(get_page_title(url))

print("\nFirst Paragraph:")
print(get_first_paragraph(url))

