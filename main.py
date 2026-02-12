from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def click_to_pizza():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(0.5)
    #Website that is being pulled
    driver.get("http://bettermotherfuckingwebsite.com/")
    driver.implicitly_wait(10)
    try:
        element = driver.find_element(By.LINK_TEXT, "grotesque pile of shit")
    except Exception as e:
        print("Could not find element: {e}")
        driver.quit()
        exit()

    actions = ActionChains(driver)
    driver.implicitly_wait(10)
    element.click()

    time.sleep(10)


    assert element is not None

    driver.quit()
    write_to_pizza()

def write_to_pizza():
    print("This is an automated test")


click_to_pizza()
write_to_pizza()


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