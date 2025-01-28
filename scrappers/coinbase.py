from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from driver.driver import gen_driver
from transformers.transform import transform_coin_base
from load.load_to_csv import load_to_csv
from load.load_to_db import load_to_db
import time


def scrape_coin_base():
    url = "https://www.coinbase.com/explore"

    driver = gen_driver()

    try:
        # driver.set_page_load_timeout(10)
        driver.get(url)

        page_no = 1
        data = []

        while True:

            time.sleep(3)
            try:
                table = driver.find_element(By.TAG_NAME, "table")

            except NoSuchElementException:
                print("Table not found")
                driver.save_screenshot("table_not_found.png")
                return

            rows = table.find_elements(By.TAG_NAME, "tr")
            # data = []

            print(f"Scraping page {page_no}...")

            for row in rows:
                # print(row)

                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text for cell in cells]
                print(row_data)

                if row_data:
                    transformed_data = transform_coin_base(row_data)
                    data.append(transformed_data)
                    # load_to_db(transformed_data)

                # print(processed_row)
                # data.append(row_data)

            try:
                next_button = driver.find_element(
                    By.XPATH, '//a[@href and contains(@href, "?page=")]'
                )
                next_button.click()
                print("Next button clicked")
                page_no += 1
            except Exception as e:
                print("Next button not found")
                print("Closing.....")
                break
        if data:
            load_to_csv(data)
            print("Data loaded to CSV successfully")
            load_to_db(data)
            print("Data loaded to database successfully")
        # return data

    except WebDriverException as e:
        print("Webdriver error: ", e)
        driver.save_screenshot("error_webdriver.png")
        driver.quit()

    finally:
        driver.quit()
    # return data
