from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from driver.driver import gen_driver

def scrape_gecko():
    url = 'https://www.coingecko.com/'

    
    driver = gen_driver()
    
    
    try:
        # driver.set_page_load_timeout(10)
        driver.get(url)
        
        try:
            table = driver.find_element(By.TAG_NAME, 'table')
        
        except NoSuchElementException:
            print('Table not found')
            driver.save_screenshot('table_not_found.png')
            return
    
        rows = table.find_elements(By.TAG_NAME, 'tr')
        data = []

        for row in rows:
            # print(row)
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text for cell in cells]
            if row_data:
                data.append(row_data)
        return data

    except WebDriverException as e:
        print("Webdriver error: ", e)   
        driver.save_screenshot('error_webdriver.png')
        driver.quit()
    
    
    
    finally:
        driver.quit()
    return data

    

