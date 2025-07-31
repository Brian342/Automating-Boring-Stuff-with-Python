# Task 2: Data Scraper
# Description: Develop a web scraper to extract specific data from a website (e.g., news headlines, product prices).

# Objectives:
# Use the request library to retrieve web page content. Parse the HTML using BeautifulSoup.
# Extract specific data, such as article titles or product details.
# Save the scraped data into a CSV file.

import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/catalog/?q=macbook+laptop"
headers = {
    'User-Agent': 'Chrome/138'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

product = soup.find_all('article', class_='prd _fb col c-prd')

for products in product:
    tag_title = products.find('h3')
    tag_price = products.find('div', class_='prc')
    if tag_title and tag_price:
        print(f"Product: {tag_title.text}, Price->{tag_price.text}", sep=' ')
