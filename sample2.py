import csv
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

# ------------------------------
# CONFIG
checkpoint_file = "checkpoint.json"
csv_file = "ciscoReviews.csv"
total_pages = 10
start_page = 1  # default if no checkpoint found
# ------------------------------

# Load checkpoint if exists
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, "r") as f:
        start_page = json.load(f).get("last_page", 1)

print(f"Resuming from page {start_page}...")

options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)
driver.get("https://www.glassdoor.com/Reviews/Cisco-Reviews-E1425.htm")

# Give the first page time to load
time.sleep(70)

# Open CSV in append mode if resuming, write header only if starting from scratch
write_header = not os.path.exists(csv_file) or start_page == 1
csv_mode = "a" if start_page > 1 else "w"

with open(csv_file, csv_mode, newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    if write_header:
        writer.writerow(['Job Title', 'Job Ratings', 'time', 'JobStatus', 'Pros', 'Cons'])

    for page in range(start_page, total_pages + 1):
        time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews = soup.find('div', id='ReviewsFeed')

        if not reviews:
            print(f"No reviews found on page {page}... Skipping!")
            continue

        review_items = reviews.select('li')
        for items in review_items:
            rating_tag = items.select_one('[data-test="review-rating-label"]')
            rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'

            time_tag = items.find('span', class_="timestamp_reviewDate__dsF9n")
            PostTime = time_tag.get_text(strip=True) if time_tag else 'N/A'

            job_tag = items.find('div', class_="text-with-icon_LabelContainer__xbtB8 text-with-icon_disableTruncationMobile__o_kha")
            job = job_tag.get_text(strip=True) if job_tag else 'N/A'

            title_tag = items.select_one('[data-test="review-avatar-label"]')
            title = title_tag.get_text(strip=True) if title_tag else 'N/A'

            Pros_tag = items.select_one('[data-test="review-text-PROS"]')
            ProsBody = Pros_tag.get_text(strip=True) if Pros_tag else 'N/A'

            cons_tag = items.select_one('[data-test="review-text-CONS"]')
            ConsBody = cons_tag.get_text(strip=True) if cons_tag else 'N/A'

            writer.writerow([title, rating, PostTime, job, ProsBody, ConsBody])

        print(f"✅ Finished page {page}")

        # Save checkpoint after each page
        with open(checkpoint_file, "w") as f:
            json.dump({"last_page": page + 1}, f)

        # Click next page
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="next-page"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            time.sleep(5)
            next_button.click()
        except Exception as e:
            print(f"⚠ Failed to go to page {page+1}: {e}")
            break

driver.quit()
print("Scraping complete.")
