from bs4 import BeautifulSoup
import requests


def save_section_headings(url):

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    # Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find the main content div
    content_div = soup.find("div", id="mw-content-text")

    # Find all h2 tags inside the main content
    headings = content_div.find_all("h2")

    excluded_words = ["references", "external links", "see also", "notes"]

    valid_headings = []

    for heading in headings:

        heading_text = heading.text.strip()

        # Remove [edit]
        heading_text = heading_text.replace("[edit]", "").strip()

        lower_text = heading_text.lower()

        # Skip unwanted headings
        skip = False
        for word in excluded_words:
            if word in lower_text:
                skip = True
                break

        if not skip and heading_text != "":
            valid_headings.append(heading_text)

    # Save headings
    with open("headings.txt", "w") as file:
        for heading in valid_headings:
            file.write(heading + "\n")

    print("Saved headings to headings.txt")


url = "https://en.wikipedia.org/wiki/Data_science"
save_section_headings(url)
