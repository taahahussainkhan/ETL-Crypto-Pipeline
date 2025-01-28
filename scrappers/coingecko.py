from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from driver.driver import gen_driver
import time
from transformers.transform import transform_coin_gecko


def scrape_gecko():
    url = "https://www.coingecko.com/?page=1"

    driver = gen_driver()

    try:
        # driver.set_page_load_timeout(10)
        driver.get(url)
        print("Scrapping CoinGecko...")

        page_no = 1
        while True:
            time.sleep(3)
            try:
                table = driver.find_element(By.TAG_NAME, "table")
            except NoSuchElementException:
                print("Table not found")
                driver.save_screenshot("table_not_found.png")
                return
            rows = table.find_elements(By.TAG_NAME, "tr")
            data = []
            print(f"Scraping page {page_no}...")
            for row in rows:
                # print(row)

                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text for cell in cells]

                if row_data:
                    # print(row_data)
                    transformed_data = transform_coin_gecko(row_data)
                    data.append(transformed_data)

            try:
                next_button = driver.find_element(
                    By.XPATH, '//a[@href and contains(@href, "?page=")]'
                )
                next_button.click()
                print("Next button clicked")
                page_no += 1

                # I am limiting the number of pages to 2 for testing purposes
                if page_no == 2:
                    break

            except Exception as e:
                print("Next button not found")
        return data

    except WebDriverException as e:
        print("Webdriver error: ", e)
        driver.save_screenshot("error_webdriver.png")
        driver.quit()

    finally:
        driver.quit()
    return data
