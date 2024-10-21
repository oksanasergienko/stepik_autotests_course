from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]').send_keys("Oks")
    last_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]').send_keys("S")
    email = browser.find_element(By.CSS_SELECTOR,'input.form-control.third[required]').send_keys("123")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # write the text from the welcome_text_elt element to the welcome_text variable
    welcome_text = welcome_text_elt.text

    # using assert we check that the expected text matches the text on the site page
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()


