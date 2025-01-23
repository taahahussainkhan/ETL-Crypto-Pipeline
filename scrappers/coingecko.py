import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def scrape_gecko():
    url = 'https://www.coingecko.com/'
    
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--disable-gpu')  
    chrome_options.add_argument('--no-sandbox')  
    chrome_options.add_argument('--disable-dev-shm-usage')  
    chrome_options.add_argument('--window-size=1920,1080') 
    
    driver = webdriver.Chrome()
    
    try:
        driver.set_page_load_timeout(10)
        driver.get(url)
        
        try:
            table = driver.find_element(By.TAG_NAME, 'table')
        
        except NoSuchElementException:
            print('Table not found')
            driver.save_screenshot('screenshot.png')
            return
    
        rows = table.find_elements(By.TAG_NAME, 'tr')
    
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            data = [cell.text for cell in cells]
            print(data)
        
    
        
        

    except WebDriverException as e:
        print("Webdriver error: ", e)   
        driver.save_screenshot('error_webdriver.png')
        driver.quit()
    
    
    
    finally:
        driver.quit()
    

