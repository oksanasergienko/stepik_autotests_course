from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first[required]').send_keys("Ok")
    last_name = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[required]').send_keys("S")
    email = browser.find_element(By.CSS_SELECTOR,'input.form-control.third[required]').send_keys("123")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

# in this test we verify that it crashes with an error:
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"input.form-control.second[required]"}

