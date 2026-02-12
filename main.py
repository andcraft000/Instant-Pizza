from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
# driver.implicity_wait(0.5)
driver.get("https://github.com/andcraft000/Instant-Pizza")

try:
    element = driver.find_element(By.CLASS_NAME, "react-directory-row-name-cell-small-screen")
except Exception as e:
    print("Could not find element: {e}")
    driver.quit()
    exit()

actions = ActionChains(driver)
element.click

time.sleep(10)


assert element is not None

driver.quit()


def orderpizza():
    print('Hello!')
    driver.quit()


# Click and release
    # clickable = driver.find_element(By.ID, "click")
    # ActionChains(driver) \
    #     .click(clickable) \
    #     .perform()

# Move to element
    # hoverable = driver.find_element(By.ID, "hover")
    # ActionChains(driver) \
    #     .move_to_element(hoverable) \
    #     .perform()

# Context Click (combines clicking & moving to an element) (Right Click)
    # clickable = driver.find_element(By.ID, "clickable")
    # ActionChains(driver) \
    #     .context_click(clickable) \
    #     .perform()

# Send Keys: Active Element
    # ActionChains(driver)\
    #     .send_keys("abc")\
    #     .perform()

# Designated Element
    # text_input = driver.find_element(By.ID, "textInput")
    # ActionChains(driver)\
    #     .send_keys_to_element(text_input, "abc")\
    #     .perform()