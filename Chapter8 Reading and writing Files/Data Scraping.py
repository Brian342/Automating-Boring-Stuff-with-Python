# # Task 2: Data Scraper
# # Description: Develop a web scraper to extract specific data from a website (e.g., news headlines, product prices).
#
# # Objectives:
# # Use the request library to retrieve web page content. Parse the HTML using BeautifulSoup.
# # Extract specific data, such as article titles or product details.
# # Save the scraped data into a CSV file.
#
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.jumia.co.ke/catalog/?q=macbook+laptop"
headers = {
    'User-Agent': 'Chrome/138'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

product = soup.find_all('article', class_='prd')

with open('Jumia_Macbook_sale.csv', 'w', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Product Name', 'Price', 'Ratings'])

    for products in product:
        tag_title = products.find('h3', class_='name')
        tag_price = products.find('div', class_='prc')
        ratings = products.find('div', class_='stars _s')

        if tag_title and tag_price:
            product_name = tag_title.text.strip()
            Price = tag_price.text.strip()
            Ratings = ratings.text.strip() if ratings else "No rating."

            print(f"{product_name} \nprice->{Price} Ratings->{Ratings}")
            writer.writerow([product_name, Price, Ratings])
