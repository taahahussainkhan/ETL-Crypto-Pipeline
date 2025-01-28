from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from driver.driver import gen_driver
import time
import csv
from database.database import insert_data


def scrape_coin_market_cap():
    url = "https://coinmarketcap.com/"

    driver = gen_driver()

    try:
        # driver.set_page_load_timeout(10)
        driver.get(url)

        with open("coin-market-cap.csv", mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "Serial No",
                    "Coin",
                    "Price",
                    "1h Change",
                    "24h Change",
                    "7d Change",
                    "24h Volume",
                    "Market Cap",
                    "Source",
                ]
            )

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
                        processed_row = [
                            row_data[1] if len(row_data) > 1 else "N/A",
                            row_data[2] if len(row_data) > 2 else "N/A",
                            row_data[4] if len(row_data) > 4 else "N/A",
                            row_data[5] if len(row_data) > 5 else "N/A",
                            row_data[6] if len(row_data) > 6 else "N/A",
                            row_data[7] if len(row_data) > 7 else "N/A",
                            row_data[8] if len(row_data) > 8 else "N/A",
                            row_data[9] if len(row_data) > 9 else "N/A",
                            "Coin Market Cap",
                        ]

                        writer.writerow(processed_row)
                        insert_data(processed_row)
                        print(processed_row)
                        data.append(row_data)

                try:
                    next_button = driver.find_element(
                        By.XPATH, '//a[@href and contains(@href, "?page=")]'
                    )
                    next_button.click()
                    print("Next button clicked")
                    page_no += 1

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
