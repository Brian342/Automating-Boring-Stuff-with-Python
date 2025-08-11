# importing modules
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.headless = False  # Set to True if you want to hide browser

driver = uc.Chrome(options=options)
driver.get(
    "https://www.glassdoor.com/Reviews/Cisco-Reviews-E1425.htm")

# Let the page load
time.sleep(70)

num_pages = 3253

with open('ciscoReviews.csv', 'w', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Job Title', 'Job Ratings', 'time', 'JobStatus', 'Pros', 'Cons'])

    for page in range(num_pages):
        time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews = soup.find('div', id='ReviewsFeed')
        if not reviews:
            print('No reviews found on this page .... Skipping!')
            continue
        review_items = reviews.select('li')
        title = soup.title.string
        # print(title)

        for items in review_items:
            rating_tag = items.select_one('[data-test="review-rating-label"]')
            rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'

            # getting the timestamp
            time_tag = items.find('span', class_="timestamp_reviewDate__dsF9n")
            PostTime = time_tag.get_text(strip=True) if time_tag else 'N/A'

            # job status
            job_tag = items.find('div',
                                 class_="text-with-icon_LabelContainer__xbtB8 text-with-icon_disableTruncationMobile__o_kha")
            job = job_tag.get_text(strip=True) if job_tag else 'N/A'

            # extracting the title
            title_tag = items.select_one('[data-test="review-avatar-label"]')
            title = title_tag.get_text(strip=True) if title_tag else 'N/A'

            # Description
            Pros_tag = items.select_one('[data-test="review-text-PROS"]')
            ProsBody = Pros_tag.get_text(strip=True) if Pros_tag else 'N/A'

            Pros_title = items.find('p', class_="review-text_textTitle__h8c3S review-text_green___30m9")
            ProsHeader = Pros_title.get_text(strip=True) if Pros_title else 'N/A'

            cons_title = items.find('p', class_="review-text_textTitle__h8c3S  review-text_red__0dGPZ")
            ConsHeader = cons_title.get_text(strip=True) if cons_title else 'N/A'

            cons_tag = items.select_one('[data-test="review-text-CONS"]')
            ConsBody = cons_tag.get_text(strip=True) if cons_tag else 'N/A'

            writer.writerow([title, rating, PostTime, job, ProsBody, ConsBody])
            print(f"wrote review")

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="next-page"]'))
            )

            # Scroll it into view to avoid interception
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            time.sleep(5)

            next_button.click()
            print("Clicked the next page button")
        except Exception as e:
            print("Failed to find or click the next page button:", e)

driver.quit()

print(f"\nTotal Reviews Scraped: {len(title)}")
print(f"Job Title: {title}")
print()
print(f"Job Ratings: {rating}")
print()
print(f"TimeStamp: {PostTime}")
print()
print(f"JobStatus: {job}")
print()
print(f"Pros: {ProsBody}")
print()
print(f"Cons: {ConsBody}")
