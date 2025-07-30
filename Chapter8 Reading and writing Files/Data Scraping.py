# Task 2: Data Scraper
# Description: Develop a web scraper to extract specific data from a website (e.g., news headlines, product prices).

# Objectives:
# Use the request library to retrieve web page content. Parse the HTML using BeautifulSoup.
# Extract specific data, such as article titles or product details.
# Save the scraped data into a CSV file.

import requests
from bs4 import BeautifulSoup
url = "https://www.jumia.co.ke/catalog/?q=macbook+laptop"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# The link tags
for link in soup.find_all('a'):
    print(link.get('href'))
