import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from utils.config_utils import *


# Function for clicking
def click(driver):
    try:
        driver.click()
        # Add color to the
        print("\033[31m" + "~~~~ CLICK ~~~~" + "\033[0m")

    except WebDriverException:
        print("Error of WebDriverException while clicking")
        return

    except Exception as e:
        print("Error while clicking: ", e)
        return


# Function for clicking on cookies popup (use wait_for_cookies_popup before and then click)
def click_on_cookies_popup(driver):
    try:
        cookies = wait_for_cookies_popup(driver)
        click(cookies)
        print("Clicked on cookies popup")
        time.sleep(5)

    except TimeoutException:
        print("Cookies popup not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on cookies popup: ", e)
        return


# Function for waiting for cookies popup
def wait_for_cookies_popup(driver):
    try:
        cookies = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")))
        print("Cookies popup found")
        time.sleep(5)
        return cookies

    except TimeoutException:
        print("Cookies popup not found")
        return

    except Exception as e:
        print("Error while waiting for cookies popup: ", e)
        return
