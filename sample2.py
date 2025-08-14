from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time, csv, undetected_chromedriver as uc

options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)
driver.get("https://www.glassdoor.com/Reviews/Cisco-Reviews-E1425.htm")
time.sleep(5)

# Go to page 1000
for i in range(999):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="next-page"]'))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
        time.sleep(1)
        next_button.click()
        print(f"Reached page {i + 2}")
        time.sleep(3)
    except Exception as e:
        print(f"Could not go to next page at step {i + 1}: {e}")
        break

# Now scrape starting from page 1000
with open('ciscoReviews.csv', 'a', newline='', encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Job Title', 'Job Ratings', 'Time', 'JobStatus', 'Pros', 'Cons'])

    while True:
        time.sleep(70)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        reviews = soup.find('div', id='ReviewsFeed')
        if not reviews:
            print('No reviews found on this page .... Skipping!')
            break

        for items in reviews.select('li'):
            rating_tag = items.select_one('[data-test="review-rating-label"]')
            rating = rating_tag.get_text(strip=True) if rating_tag else 'N/A'

            time_tag = items.find('span', class_="timestamp_reviewDate__dsF9n")
            PostTime = time_tag.get_text(strip=True) if time_tag else 'N/A'

            job_tag = items.find('div',
                                 class_="text-with-icon_LabelContainer__xbtB8 text-with-icon_disableTruncationMobile__o_kha")
            job = job_tag.get_text(strip=True) if job_tag else 'N/A'

            title_tag = items.select_one('[data-test="review-avatar-label"]')
            job_title = title_tag.get_text(strip=True) if title_tag else 'N/A'

            Pros_tag = items.select_one('[data-test="review-text-PROS"]')
            ProsBody = Pros_tag.get_text(strip=True) if Pros_tag else 'N/A'

            cons_tag = items.select_one('[data-test="review-text-CONS"]')
            ConsBody = cons_tag.get_text(strip=True) if cons_tag else 'N/A'

            writer.writerow([job_title, rating, PostTime, job, ProsBody, ConsBody])
            print(f"Wrote review for {job_title}")

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="next-page"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
            time.sleep(1)
            next_button.click()
        except Exception as e:
            print("No more pages:", e)
            break

driver.quit()
