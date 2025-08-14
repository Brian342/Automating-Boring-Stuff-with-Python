import csv, time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

LAST_PAGE_FILE = "last_page.txt"
CSV_FILE = "ciscoReviews2.csv"


# Function to read last page from file (or start at 1 if a file missing)
def get_start_page():
    if os.path.exists(LAST_PAGE_FILE):
        with open(LAST_PAGE_FILE, "r") as f:
            return int(f.read().strip())
    return 1


# Function to save current page number to file
def save_last_page(page_number):
    with open(LAST_PAGE_FILE, "w") as f:
        f.write(str(page_number))


# Start Chrome
options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)

# Start from saved page
start_page = get_start_page()
url = f"https://www.glassdoor.com/Reviews/Cisco-Reviews-E1425_P{start_page}.htm"
driver.get(url)
time.sleep(70)

# Open CSV in append mode
file_exists = os.path.exists(CSV_FILE)
with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    if not file_exists:
        writer.writerow(['Job Title', 'Job Ratings', 'Time', 'JobStatus', 'Pros', 'Cons'])

    current_page = start_page
    while True:
        save_last_page(current_page)  # save progress
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        reviews = soup.find('div', id='ReviewsFeed')

        if not reviews:
            print(f"No reviews found on page {current_page}, stopping.")
            break

        review_items = reviews.select('li')
        for items in review_items:
            rating_tag = items.select_one('[data-test="review-rating-label"]')
            rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'

            time_tag = items.find('span', class_="timestamp_reviewDate__dsF9n")
            post_time = time_tag.get_text(strip=True) if time_tag else 'N/A'

            job_tag = items.find('div',
                                 class_="text-with-icon_LabelContainer__xbtB8 text-with-icon_disableTruncationMobile__o_kha")
            job_status = job_tag.get_text(strip=True) if job_tag else 'N/A'

            title_tag = items.select_one('[data-test="review-avatar-label"]')
            job_title = title_tag.get_text(strip=True) if title_tag else 'N/A'

            pros_tag = items.select_one('[data-test="review-text-PROS"]')
            pros_body = pros_tag.get_text(strip=True) if pros_tag else 'N/A'

            cons_tag = items.select_one('[data-test="review-text-CONS"]')
            cons_body = cons_tag.get_text(strip=True) if cons_tag else 'N/A'

            writer.writerow([job_title, rating, post_time, job_status, pros_body, cons_body])
            print(f"✅ Page {current_page}: Wrote review for {job_title}")

        # Try clicking Next page
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="next-page"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            time.sleep(5)
            next_button.click()
            current_page += 1
            print(f"➡️ Moving to page {current_page}")
        except Exception:
            print("🚫 No more pages — scraping complete.")
            break

driver.quit()
print("✅ Finished scraping!")
