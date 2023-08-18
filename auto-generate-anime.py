from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # first page url
    current_url = input("please enter the first page url: ")
    # current_url = "https://www.cartoonmad.com/comic/765400912019001.html"
    
    while(1):
        driver.get(current_url) # open url
        driver.execute_script("document.body.style.zoom = '50%'")   # adjust driver size

        time.sleep(6)   # read duration

        ## next page
        body = driver.find_element("tag name", "body") 
        body.send_keys(Keys.ARROW_RIGHT)
        
        ## if last page, next chapter
        if current_url == driver.current_url:
            css_selector = ".pages"
            element = driver.find_element(By.CSS_SELECTOR, css_selector)
            driver.execute_script("arguments[0].click();", element)

        current_url = driver.current_url

finally:
    driver.close()