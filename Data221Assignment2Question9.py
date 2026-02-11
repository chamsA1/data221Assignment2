from bs4 import BeautifulSoup
import requests
import csv


def save_table(url):

    # Download page (pretend to be browser)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # Find main content div
    content = soup.find("div", id="mw-content-text")

    # Stop if content not found
    if content is None:
        print("Main content not found")
        return


    tables = content.find_all("table")


    # Find first table with 3+ data rows
    for table in tables:

        rows = table.find_all("tr")

        data_rows = [r for r in rows if r.find_all("td")]

        if len(data_rows) >= 3:
            chosen_table = table
            break
    else:
        print("No valid table found")
        return


    # Get headers
    headers = []

    header_cells = chosen_table.find_all("th")

    if header_cells:
        for cell in header_cells:
            headers.append(cell.text.strip())


    # Get data
    table_data = []
    max_cols = 0

    for row in chosen_table.find_all("tr"):

        cells = row.find_all("td")

        if not cells:
            continue

        values = [c.text.strip() for c in cells]

        table_data.append(values)

        max_cols = max(max_cols, len(values))


    # Create headers if missing
    if not headers:
        headers = ["col" + str(i+1) for i in range(max_cols)]


    # Pad rows
    for row in table_data:
        while len(row) < max_cols:
            row.append("")


    # Save CSV
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        writer.writerows(table_data)


    print("Saved wiki_table.csv")


url = "https://en.wikipedia.org/wiki/Machine_learning"

save_table(url)
