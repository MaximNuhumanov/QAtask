import time

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def selenium_magick():
    print('selentium magik start')

    CHROMEDRIVERPASS = 'D:\QAproj\chromedriver.exe'
    service = ChromeService(executable_path=CHROMEDRIVERPASS)
    driver = webdriver.Chrome(service=service)

    print('open site')
    driver.get('https://rozetka.com.ua/')

    time.sleep(2)

    print('enter query to search field')
    search_input = driver.find_element(By.CSS_SELECTOR, "input[name = 'search']")
    search_input.send_keys('Xiaomi')
    search_input.send_keys(Keys.ENTER)
    
    time.sleep(3)

    print('click on first item')
    driver.find_element(By.XPATH, ".//span[@class='goods-tile__title']/parent::a").click()

    time.sleep(3)
    product_title = driver.find_element(By.CSS_SELECTOR,"h1.product__title")

    assert 'Xiaomi' in product_title.text

    time.sleep(3)
    product_id = driver.find_element(By.XPATH,".//p[@class = 'product__code detail-code']")
  
    assert product_id.text is not None



    time.sleep(10)
        
    print('close bowser')
    driver.quit()


    print('Selentium Magic Ends')

if __name__ == "__main__":
    selenium_magick()