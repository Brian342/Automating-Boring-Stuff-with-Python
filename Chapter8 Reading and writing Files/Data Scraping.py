# Task 2: Data Scraper
# Description: Develop a web scraper to extract specific data from a website (e.g., news headlines, product prices).

# Objectives:
# Use the request library to retrieve web page content. Parse the HTML using BeautifulSoup.
# Extract specific data, such as article titles or product details.
# Save the scraped data into a CSV file.

import requests
from bs4 import BeautifulSoup
url = ""
soup = BeautifulSoup()