import time

# webdriver is a set of commands for controlling the browser
from selenium import webdriver

# import the By class, which allows you to choose how to search for an element
from selenium.webdriver.common.by import By

# initialize the browser driver. After this command you should see a new browser window open
driver = webdriver.Chrome()

# the time.sleep command sets a pause of 5 seconds so that we have time to see what is happening in the browser
time.sleep(5)

# The get method tells the browser to open the site at the specified link
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# The find_element method allows you to find the element on the site by specifying the path to it
# The method takes as arguments the search method and the value by which we will search
# search for the text input field
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# write the answer in the found field
textarea.send_keys("get()")
time.sleep(5)

# find a button that sends the entered solution
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# tell the driver to press the button. After this command we should see a message about the correct answer
submit_button.click()
time.sleep(5)

# after completing all the steps, we must not forget to close the browser window
driver.quit()


