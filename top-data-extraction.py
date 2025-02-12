import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://clincalc.com/DrugStats/Top300Drugs.aspx"

# Requesting the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Finding the table on the webpage
table = soup.find("table", {"id": "tableTopDrugs"})

# Extracting table headers
headers = [th.text.strip() for th in table.find_all("th")]

# Extracting table rows
rows = []
for tr in table.find_all("tr")[1:]:  # Skipping the header row
    cells = [td.text.strip() for td in tr.find_all("td")]
    if cells:
        rows.append(cells)

# Creating a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Saving to CSV
df.to_csv("top_300_drugs.csv", index=False)

print("CSV file saved as 'top_300_drugs.csv'")
