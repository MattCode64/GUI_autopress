import time
import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from utils.config_utils import get_json_file


def click(driver):
    try:
        driver.click()
        print("\033[31m" + "~~~~ CLICK ~~~~" + "\033[0m")

    except WebDriverException:
        print("Error of WebDriverException while clicking")
        return

    except Exception as e:
        print("Error while clicking: ", e)
        return


def wait_for_element(driver, XPATH):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPATH)))
        print("Element found")
        time.sleep(2)
        return element

    except TimeoutException:
        print("Element not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while waiting for element: ", e)
        return


def click_on_read_newspaper(driver):
    try:
        XPATH_READ_NEWSPAPER = get_json_file("lacroix")["read"]["full_XPATH"]

        read_newspaper = wait_for_element(driver, XPATH_READ_NEWSPAPER)
        print("Read newspaper found")

        click(read_newspaper)
        print("Clicked on read newspaper")
        time.sleep(0.5)

    except TimeoutException:
        print("Read newspaper not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on read newspaper: ", e)
        return


def click_on_login_button(driver):
    try:
        XPATH_LOGIN_BUTTON = get_json_file("lacroix")["login"]["full_XPATH"]

        login_button = wait_for_element(driver, XPATH_LOGIN_BUTTON)
        print("Login button found")

        click(login_button)
        print("Clicked on login button")
        time.sleep(0.5)

    except TimeoutException:
        print("Login button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on login button: ", e)
        return


def click_on_keep_me_logged_in(driver):
    try:
        XPATH_KEEP_ME_LOGGED_IN = get_json_file("lacroix")["keep_logged_in"]["full_XPATH"]

        keep_me_logged_in = wait_for_element(driver, XPATH_KEEP_ME_LOGGED_IN)
        print("Keep me logged in found")

        click(keep_me_logged_in)
        print("Clicked on keep me logged in (Unchecked)")
        time.sleep(.5)

    except TimeoutException:
        print("Keep me logged in not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on keep me logged in: ", e)
        return


def input_email_password(driver):
    try:
        XPATH_EMAIL = get_json_file("lacroix")["email"]["full_XPATH"]
        XPATH_PASSWORD = get_json_file("lacroix")["password"]["full_XPATH"]

        email_field = wait_for_element(driver, XPATH_EMAIL)
        print("Email field found")
        time.sleep(0.2)

        password_field = wait_for_element(driver, XPATH_PASSWORD)
        print("Password field found")
        time.sleep(0.2)

        # Wait for email and password field
        # email_field, password_field = wait_email_password(driver)

        # Get email and password
        email, password = get_email_password()

        # Input email and password
        input_text(email_field, email)
        print("Email inputted")
        input_text(password_field, password)
        print("Password inputted")

        print("~~~ Email and password inputted ~~~")

    except Exception as e:
        print("Error while inputting email and password: ", e)
        return


def input_text(driver, text):
    try:
        driver.send_keys(text)
        # Add color to the
        print("\033[31m" + "~~~~ INPUT TEXT ~~~~" + "\033[0m")

    except WebDriverException:
        print("Error of WebDriverException while inputting text")
        return

    except Exception as e:
        print("Error while inputting text: ", e)
        return


def get_email_password():
    try:
        load_dotenv()
        email = os.getenv("LACROIX_EMAIL")
        password = os.getenv("LACROIX_PASSWORD")

        if email and password:
            print("Email and password are not empty")
            return email, password

        else:
            print("Email and password are empty")
            return

    except Exception as e:
        print("Error while getting email and password: ", e)
        return


def clik_on_se_connecter_button(driver):
    try:
        XPATH_SE_CONNECTER_BUTTON = get_json_file("lacroix")["se_connecter_button"]["full_XPATH"]

        se_connecter_button = wait_for_element(driver, XPATH_SE_CONNECTER_BUTTON)
        print("Se connecter button found")

        click(se_connecter_button)
        print("Clicked on se connecter button")
        time.sleep(0.5)

    except TimeoutException:
        print("Se connecter button not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on se connecter button: ", e)
        return


def click_on_cookies_popup(driver):
    try:
        XPATH_COOKIES_POPUP = get_json_file("lacroix")["cookies_button"]["full_XPATH"]

        cookies = wait_for_element(driver, XPATH_COOKIES_POPUP)
        print("Cookies popup found")
        click(cookies)
        print("Clicked on cookies popup")
        time.sleep(0.5)

    except TimeoutException:
        print("Cookies popup not found (TimeoutException)")
        return

    except Exception as e:
        print("Error while clicking on cookies popup: ", e)
        return


def navigation(driver):
    print("Navigation")

    click_on_cookies_popup(driver)

    # Click on se connecter button
    clik_on_se_connecter_button(driver)

    # Email and password
    input_email_password(driver)

    # Click on keep me logged in
    click_on_keep_me_logged_in(driver)

    # Click on login button
    click_on_login_button(driver)

    # Click on read newspaper
    click_on_read_newspaper(driver)

    time.sleep(15)
